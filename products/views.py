from django.shortcuts import render
from json import load
from datetime import datetime

# Create your views here.
from geekshop.settings import BASE_DIR


def index(requests):
    context = {'title': 'GeekShop Store'}
    return render(requests, 'products/index.html', context)


def products(requests):
    """
    :param requests:
    :return:
    """
    with open(BASE_DIR / 'products/fixtures/products.json', 'r', encoding='utf-8') as f:
        context = load(f)
        context['year'] = datetime.now().year
        context['title'] = 'Products'
        return render(requests, 'products/products.html', context)
