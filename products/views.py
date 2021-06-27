from django.shortcuts import render
from json import load
from datetime import datetime


# Create your views here.


def index(requests):
    context = {'title': 'GeekShop Store'}
    return render(requests, 'products/index.html', context)


def products(requests):
    """
    :param requests:
    :return:
    """
    # сработал только абсолютный путь
    with open('C:\\Users\\Terramora.CNV\\Documents\\GitHub\\Django\\geekshop\\products\\fixtures\\products.json', 'r',
              encoding='utf-8') as f:
        context = load(f)
        context['year'] = datetime.now().year
        return render(requests, 'products/products.html', context)
