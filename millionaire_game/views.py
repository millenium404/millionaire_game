# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from articles.models import


@login_required
def home_view(request):
    context = {}
    return render(request, 'home-view.html', context)
