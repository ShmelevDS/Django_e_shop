from django.shortcuts import render
from .models import Product, Icon
from django.conf import settings


def main(request):
    products = Product.objects.all()
    icons = Icon.objects.all()

    content = {"container_name": 'container',
               'title': 'shopy - home',
               'media_url': settings.MEDIA_URL,
               'products': products,
               'icons': icons}

    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {'title': 'shopy - products',
               "container_name": 'products-container'}

    return render(request, 'mainapp/products.html', content)


def contacts(request):
    content = {"container_name": 'contacts-container',
               'title': 'shopy - contacts'}

    return render(request, 'mainapp/contacts.html', content)
