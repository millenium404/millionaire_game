from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True)
    games_played = models.FloatField(max_length=50, blank=True, null=True)
    total_score = models.FloatField(max_length=50, blank=True, null=True)
    average_score = models.FloatField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.user.username}'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
