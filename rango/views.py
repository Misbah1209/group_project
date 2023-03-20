from django.http import HttpResponse
from rango.models import Category, Product, Order
from rango.forms import UserForm, UserProfileForm, CategoryForm, ProductForm, OrderForm
from django.shortcuts import redirect, render
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    # this method is used to display the index page along with list of all category
    category_list = Category.objects.all
    context_dict = {}
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def show_category(request,category_name_slug):
    # this method is used to display the products of a specific category and perform search, sort and filter
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
    # this method is used to register user and save their detail to the database
    category_list = Category.objects.all
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        # check if the details are entered correctly
        if user_form.is_valid() and profile_form.is_valid():
            #once form is validated save the details in the database
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            registered = True
            return redirect(reverse('rango:register_completed'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'rango/register.html', context = {'user_form': user_form,'profile_form': profile_form,
                                        'registered': registered,'categories':category_list})

def user_login(request):
    # this method is used to allow user login using their username and password.
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
    # this method is used to perform log out
    logout(request)
    return redirect(reverse('rango:index'))

def cart(request):
    # this method is used to save the information of the users cart
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
    #this funtion helps to load the admin page and provides access to add category and product
    category_list = Category.objects.all
    order_list = Order.objects.all
    return render(request, 'rango/admin_profile.html', context={'categories':category_list,'orders':order_list})

def add_category(request):
    # this method is used to add new category to the existing list
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
    # this method is used to add new category to the existing list
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

def register_completed(request):
    # this method is used to display the registeration completed page along with list of all category
    category_list = Category.objects.all
    context_dict = {}
    context_dict['categories'] = category_list
    return render(request, 'rango/register_completed.html',context=context_dict)
