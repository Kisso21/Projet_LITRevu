from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # URL pour le flux d'activités
    path('flux/', views.flux, name='flux'),
        # URL pour créer un nouveau billet
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    # URL pour gérer les abonnements
    path('subscriptions/', views.manage_subscriptions, name='subscriptions'),
    # URL pour la connexion
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # URL pour l'inscription
    path('signup/', views.signup, name='signup'),
    # URL pour la déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # URL racine pointant vers la vue 'home'
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # URL pour le tableau de bord
    path('create_ticket_and_review/', views.create_ticket_and_review, name='create_ticket_and_review'),  # URL pour créer un billet avec une critique
    path('subscriptions/', views.manage_subscriptions, name='manage_subscriptions'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add_review/<int:ticket_id>/', views.add_review, name='add_review'),
    path('general-flux/', views.general_flux, name='general_flux'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
