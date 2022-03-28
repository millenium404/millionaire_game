from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    games_played = models.IntegerField(blank=True, default=0)
    total_score = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.id} - {self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
