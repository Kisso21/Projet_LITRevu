from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre du livre',
            'description': 'Description (facultatif)',
            'image': 'Image (facultatif)',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'body']
        labels = {
            'rating': 'Note',
            'body': 'Critique',
        }

class TicketReviewForm(forms.Form):
    # Formulaire combiné pour créer un billet et une critique
    ticket = TicketForm()
    review = ReviewForm()
