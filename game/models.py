from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    difficulty_choices = [('easy', 'easy'), ('normal', 'normal'), ('hard', 'hard')]
    question = models.TextField(blank=True)
    correct_answer = models.CharField(max_length=40, blank=True)
    answer_2 = models.CharField(max_length=40, blank=True)
    answer_3 = models.CharField(max_length=40, blank=True)
    answer_4 = models.CharField(max_length=40, blank=True)
    difficulty = models.CharField(max_length=10, choices=difficulty_choices)

    def __str__(self):
        return f'{self.difficulty} - {self.id} - {self.correct_answer}'


class GameSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qustions_list = models.CharField(max_length=40, blank=True, null=True)
    last_answered_question = models.IntegerField(default=0)
    game_finished = models.BooleanField(default=False)
    jokers_used = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.user.username}'