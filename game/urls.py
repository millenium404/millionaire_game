from django.urls import path, include
from .views import start_game_view


urlpatterns = [
    path('', start_game_view, name='start-game'),
]
