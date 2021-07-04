from django.shortcuts import render
from products.models import Product, ProductCategory
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
    context = {'products': Product.objects.all(),
               'categories': ProductCategory.objects.all(),
               'year': datetime.now().year,
               'title': 'Products'}
    return render(requests, 'products/products.html', context)
