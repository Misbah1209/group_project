from django.http import HttpResponse
from rango.models import Category, Product
from rango.forms import UserForm, UserProfileForm, CategoryForm, ProductForm, OrderForm
from django.shortcuts import redirect, render
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    category_list = Category.objects.all
    context_dict = {}
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def show_category(request,category_name_slug):

    kw = request.GET.get("keyword", None)
    px = request.GET.get("sort",None)
    yanse = request.GET.get("color",None)

    if kw:
        context_dict = {}
        category_list = Category.objects.all
        context_dict['categories'] = category_list
        try:
            category = Category.objects.get(slug=category_name_slug)
            if kw.isdigit():
                print(kw)
                products = Product.objects.filter(category=category,price__in=kw)
                context_dict['products'] = products
                context_dict['category'] = category
            else:
                products = Product.objects.filter(category=category,title__contains=kw)
                context_dict['products'] = products
                context_dict['category'] = category
        except Category.DoesNotExist:
            context_dict['category'] = None
            context_dict['products'] = None
        return render(request, 'rango/category_products.html', context=context_dict)
    else:
        if px == 'sx':
            print(px)
            context_dict = {}
            category_list = Category.objects.all
            context_dict['categories'] = category_list
            try:
                category = Category.objects.get(slug=category_name_slug)
                products = Product.objects.filter(category=category).order_by('price')
                print(category_name_slug,category)
                context_dict['products'] = products
                context_dict['category'] = category
            except Category.DoesNotExist:
                context_dict['category'] = None
                context_dict['products'] = None
            return render(request, 'rango/category_products.html', context=context_dict)
        elif px == 'jx' :
            print(px)
            context_dict = {}
            category_list = Category.objects.all
            context_dict['categories'] = category_list
            try:
                category = Category.objects.get(slug=category_name_slug)
                products = Product.objects.filter(category=category).order_by('-price')
                print(category_name_slug,category)
                context_dict['products'] = products
                context_dict['category'] = category
            except Category.DoesNotExist:
                context_dict['category'] = None
                context_dict['products'] = None
            return render(request, 'rango/category_products.html', context=context_dict)
        context_dict = {}
        category_list = Category.objects.all
        context_dict['categories'] = category_list
        try:
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category).order_by('price')
            print(category_name_slug, category)
            context_dict['products'] = products
            context_dict['category'] = category
        except Category.DoesNotExist:
            context_dict['category'] = None
            context_dict['products'] = None

        print(yanse)
        if yanse == 'black':
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category, color='Black')
            context_dict['products'] = products
            context_dict['category'] = category
            return render(request, 'rango/category_products.html', context=context_dict)
        elif yanse == 'white':
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category, color='White')
            context_dict['products'] = products
            context_dict['category'] = category
            return render(request, 'rango/category_products.html', context=context_dict)
        elif yanse == 'grey':
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category, color='Grey')
            context_dict['products'] = products
            context_dict['category'] = category
            return render(request, 'rango/category_products.html', context=context_dict)
        elif yanse == 'gold':
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category, color='Gold')
            context_dict['products'] = products
            context_dict['category'] = category
            return render(request, 'rango/category_products.html', context=context_dict)
        elif yanse == 'brown':
            category = Category.objects.get(slug=category_name_slug)
            products = Product.objects.filter(category=category, color='Brown')
            context_dict['products'] = products
            context_dict['category'] = category
            return render(request, 'rango/category_products.html', context=context_dict)

        return render(request, 'rango/category_products.html', context=context_dict)

def register(request):
    category_list = Category.objects.all
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'rango/register.html', context = {'user_form': user_form,'profile_form': profile_form,
                                        'registered': registered,'categories':category_list})

def user_login(request):
    category_list = Category.objects.all
    if request.method == 'POST':     
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user: 
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")     
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:     
        return render(request, 'rango/login.html',context={'categories':category_list}) 

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:index'))

def cart(request):
    category_list = Category.objects.all
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/cart.html',  {'form': form,'categories':category_list})

def admin_page(request):
    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    return render(request, 'rango/admin_profile.html', context=context_dict)

def add_category(request):
    category_list = Category.objects.all
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat=form.save(commit=True)
            print(cat.slug)
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form,'categories':category_list})

def add_product(request):
    category_list = Category.objects.all
    form = ProductForm()
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/rango/')
        else:
            print(form.errors)
    return render(request,'rango/add_product.html',{'form': form,'categories':category_list})
