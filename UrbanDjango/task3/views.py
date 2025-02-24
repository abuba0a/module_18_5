from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def home_page(request):
    title = 'Play'
    headline = 'Главная страница'
    context = {
        'title': title,
        'headline': headline,
    }
    return render(request, 'platform.html', context)


def game_page(request):
    title = 'Games'
    text = 'Игры'
    pay = 'Купить'
    context = {
        'title': title,
        'text': text,
        'pay': pay,
    }
    return render(request, 'games.html', context)


def cart_page(request):
    title = 'Cart'
    text = 'Корзина для новых опций'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'cart.html', context)
