from django.shortcuts import render
from store.models import Game


def home(request):
    return render(request, 'store/home.html')


def game_detail(request, game_id):
    # Получите информацию о конкретной игре из базы данных (по её ID)
    game = Game.objects.get(id=game_id)
    # Здесь вы можете передать информацию о игре в шаблон и отобразить её
    return render(request, 'games/game_detail.html', {'game': game})
