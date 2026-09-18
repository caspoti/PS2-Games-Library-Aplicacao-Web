from django.shortcuts import render, get_object_or_404
from ps2.models import Game
from django.views.generic import CreateView
from ps2.forms import GameModelForm

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


# Class Create based view
class NewGameCreateView(CreateView):

    model = Game
    form_class = GameModelForm
    template_name = 'new_game.html'
    success_url = '/games/'

    # 'form' é a variavel nativa do CreateView, usa-se como contexto dentro do new_game.html
