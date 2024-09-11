from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Ticket, Review, UserFollows
from .forms import TicketForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TicketForm, ReviewForm, TicketReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from itertools import chain
from django.db.models import Q
from operator import attrgetter


# Vue pour la page d'accueil où les utilisateurs peuvent s'enregistrer ou se connecter
def home(request):
    return render(request, 'litrevuweb/home.html')

# Vue pour l'inscription d'un nouvel utilisateur
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte l'utilisateur après l'inscription
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'litrevuweb/signup.html', {'form': form})

@login_required
def general_flux(request):
    # Récupérer les 10 derniers billets et critiques
    latest_tickets = Ticket.objects.all().order_by('-time_created')[:10]
    latest_reviews = Review.objects.all().order_by('-time_created')[:10]

    # Fusionner les billets et critiques dans une seule liste
    latest_items = []
    user_reviews = []

    for ticket in latest_tickets:
        latest_items.append({
            'type': 'ticket',
            'item': ticket,
        })
        # Vérifier si l'utilisateur a déjà posté une critique pour ce billet
        user_has_reviewed = Review.objects.filter(ticket=ticket, user=request.user).exists()
        user_reviews.append({
            'ticket_id': ticket.id,
            'has_reviewed': user_has_reviewed,
        })
        
    for review in latest_reviews:
        latest_items.append({
            'type': 'review',
            'item': review,
        })

    # Trier les billets et critiques par date de création
    latest_items = sorted(latest_items, key=lambda x: x['item'].time_created, reverse=True)

    # Gérer les abonnements et la création de critiques
    if request.method == 'POST':
        follow_user_id = request.POST.get('follow_user_id')
        unfollow_user_id = request.POST.get('unfollow_user_id')
        ticket_id = request.POST.get('ticket_id')

        # Gérer l'abonnement
        if follow_user_id:
            followed_user = User.objects.get(id=follow_user_id)
            UserFollows.objects.create(user=request.user, followed_user=followed_user)
            return redirect('general_flux')
        
        if unfollow_user_id:
            UserFollows.objects.filter(user=request.user, followed_user_id=unfollow_user_id).delete()
            return redirect('general_flux')

        # Gérer la création de critiques
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(id=ticket_id)
            review.save()
            return redirect('general_flux')
    else:
        form = ReviewForm()

    # Récupérer les abonnements de l'utilisateur
    user_follows_ids = UserFollows.objects.filter(user=request.user).values_list('followed_user_id', flat=True)

    return render(request, 'litrevuweb/general_flux.html', {
        'latest_items': latest_items,  # Passer la liste fusionnée
        'form': form,
        'user_follows_ids': user_follows_ids,
        'user_reviews': user_reviews,  # Liste des billets avec indication si l'utilisateur a posté une critique
    })

@login_required
def dashboard(request):
    user = request.user
    
    # Récupérer les billets créés par l'utilisateur
    user_tickets = Ticket.objects.filter(user=user).order_by('-time_created')
    
    # Récupérer les critiques faites par l'utilisateur
    user_reviews = Review.objects.filter(user=user).order_by('-time_created')
    
    # Compter le nombre de billets et de critiques
    total_tickets = user_tickets.count()
    total_reviews = user_reviews.count()
    
    return render(request, 'litrevuweb/dashboard.html', {
        'tickets': user_tickets,
        'reviews': user_reviews,
        'total_tickets': total_tickets,
        'total_reviews': total_reviews,
    })

def create_ticket_and_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect('dashboard')
    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()
    return render(request, 'litrevuweb/create_ticket_and_review.html', {
        'ticket_form': ticket_form,
        'review_form': review_form
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirige vers le tableau de bord après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def add_review(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Vérifier si l'utilisateur a déjà posté une critique pour ce ticket
    existing_review = Review.objects.filter(ticket=ticket, user=request.user).first()
    if existing_review:
        messages.error(request, "Vous avez déjà posté une critique pour ce billet.")
        return redirect('flux')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            messages.success(request, "Votre critique a été ajoutée avec succès.")
            return redirect('flux')
    else:
        form = ReviewForm()

    return render(request, 'litrevuweb/add_review.html', {'form': form, 'ticket': ticket})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.user == ticket.user:
        ticket.delete()
        return redirect('flux')
    else:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer ce billet.")
    
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if request.user == review.user:
        review.delete()
        return redirect('flux')
    else:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer cette critique.")

@login_required
def flux(request):
    user = request.user
    
    # Obtenir les utilisateurs suivis
    followed_users = UserFollows.objects.filter(user=user).values_list('followed_user', flat=True)
    
    # Billets des utilisateurs suivis et de l'utilisateur connecté
    tickets = Ticket.objects.filter(Q(user__in=followed_users) | Q(user=user)).order_by('-time_created')
    
    # Critiques des utilisateurs suivis, et critiques sur les billets de l'utilisateur connecté
    reviews = Review.objects.filter(Q(user__in=followed_users) | Q(ticket__user=user)).order_by('-time_created')
    
    # Fusionner les billets et critiques dans une seule liste triée
    combined_items = sorted(
        [{'type': 'ticket', 'content': ticket} for ticket in tickets] +
        [{'type': 'review', 'content': review} for review in reviews],
        key=lambda x: x['content'].time_created,
        reverse=True
    )
    
    return render(request, 'litrevuweb/flux.html', {'combined_items': combined_items})
@login_required
def manage_subscriptions(request):
    search_query = request.GET.get('search', '')
    found_users = []
    error_message = ''

    if search_query:
        # Recherche d'utilisateurs par nom d'utilisateur
        found_users = User.objects.filter(username__icontains=search_query).exclude(id=request.user.id)
    
    # Les utilisateurs auxquels l'utilisateur connecté est abonné
    subscriptions = UserFollows.objects.filter(user=request.user)
    
    # Les utilisateurs qui sont abonnés à l'utilisateur connecté
    subscribers = UserFollows.objects.filter(followed_user=request.user)

    if request.method == 'POST':
        follow_username = request.POST.get('follow_username')
        unfollow_user_id = request.POST.get('unfollow_user_id')
        
        if follow_username:
            try:
                followed_user = User.objects.get(username=follow_username)
                if not UserFollows.objects.filter(user=request.user, followed_user=followed_user).exists():
                    UserFollows.objects.create(user=request.user, followed_user=followed_user)
                    return redirect('manage_subscriptions')
                else:
                    error_message = f"Vous suivez déjà {followed_user.username}."
            except User.DoesNotExist:
                error_message = f"L'utilisateur {follow_username} n'existe pas."
        
        if unfollow_user_id:
            UserFollows.objects.filter(user=request.user, followed_user_id=unfollow_user_id).delete()
            return redirect('manage_subscriptions')

    context = {
        'found_users': found_users,
        'subscriptions': subscriptions,
        'subscribers': subscribers,
        'search_query': search_query,
        'error_message': error_message,
    }

    return render(request, 'litrevuweb/abonnement.html', context)

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    else:
        form = TicketForm()
    return render(request, 'litrevuweb/create_ticket.html', {'form': form})

@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    
    if request.user != ticket.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier ce billet.")
    
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('flux')
    else:
        form = TicketForm(instance=ticket)
    
    return render(request, 'litrevuweb/edit_ticket.html', {'form': form, 'ticket': ticket})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    
    if request.user != review.user:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier cette critique.")
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('flux')
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'litrevuweb/edit_review.html', {'form': form, 'review': review})
