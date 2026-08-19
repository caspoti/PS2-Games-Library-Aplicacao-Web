from django.shortcuts import render, get_object_or_404
from ps2.models import Game

# Create your views here.
def games_view(request):
    games = Game.objects.all().order_by('title')

    search = request.GET.get('search')

    if search:
        games = Game.objects.filter(title__icontains = search)

    return render(
        request,
        'games.html',
        {'games':games}
    )

def favorite_view(request):
    favorites = Game.objects.filter(favorite=True).order_by('title')

    return render(
        request,
        'favorite.html',
        {'favorites':favorites}
    )

def game_details_view(request, game_id):
    game = get_object_or_404(Game, id = game_id)

    return render(
        request,
        'game.html',
        {'game':game}
    )