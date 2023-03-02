from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'pagename': 'Home'}
    return render(request, 'rango/index.html', context=context_dict)

def product(request):
    context_dict = {'pagename': 'Product'}
    return render(request, 'rango/products.html', context=context_dict)

def register(request):
    context_dict = {'pagename': 'Register'}
    return render(request, 'rango/register.html', context=context_dict)

def login(request):
    context_dict = {'pagename': 'Login'}
    return render(request, 'rango/login.html', context=context_dict)