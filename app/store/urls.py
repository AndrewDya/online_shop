from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail')  # Изменено имя URL-шаблона
    # Другие маршруты для других страниц магазина
]
