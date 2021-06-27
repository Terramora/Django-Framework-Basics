from django.shortcuts import render
from geekshop.settings import BASE_DIR
from json import load
from pathlib import Path


# Create your views here.


def index(requests):
    return render(requests, 'products/index.html')


def products(requests):
    """
    :param requests:
    :return:
    """
    # сработал только абсолютный путь
    with open('C:\\Users\\Terramora.CNV\\Documents\\GitHub\\Django\\geekshop\\products\\fixtures\\products.json', 'r',
              encoding='utf-8') as f:
        context = load(f)
        return render(requests, 'products/products.html', context)
