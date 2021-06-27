from django.shortcuts import render


# Create your views here.


def index(requests):
    return render(requests, 'products/index.html')


def products(requests):
    return render(requests, 'products/products.html')
