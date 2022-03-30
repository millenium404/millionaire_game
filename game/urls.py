from django.urls import path, include
from .views import start_game_view, check_answer_view, end_game_view, jocker_view


urlpatterns = [
    path('', start_game_view, name='start-game'),
    path('end-game/', end_game_view, name='end-game'),
    path(r'^check-answer/(?P<answer>\w{0,50})/$', check_answer_view, name='check-answer'),
    path('use-jocker/<int:id>', jocker_view, name='use-jocker'),
]
