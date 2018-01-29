from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Game

def home(request):
    games  = Game.objects.all()
    return render(request, 'home.html', {'games':games})

def game_detail(request, id):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404('Game not found')
    return render(request, 'game_detail.html', {'game': game})
