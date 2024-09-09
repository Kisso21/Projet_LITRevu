from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

class UserFollows(models.Model):
    # Modèle représentant une relation de suivi entre deux utilisateurs
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        # Contrainte pour s'assurer qu'un utilisateur ne suit pas plusieurs fois la même personne
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"
