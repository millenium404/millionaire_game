from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def start_game_view(request):
    context = {}
    return render(request, 'game/start_game.html', context)
