from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Product
from rango.forms import UserForm, UserProfileForm

def index(request):
    category_list = Category.objects.all
    context_dict = {}
    context_dict['categories'] = category_list

    return render(request, 'rango/index.html', context=context_dict)

def show_category(request,category_name_slug):
    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    try:
        category = Category.objects.get(slug=category_name_slug)
        products = Product.objects.filter(category=category)
        context_dict['products'] = products
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None    
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

def login(request):
    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    return render(request, 'rango/login.html', context=context_dict)

def cart(request):
    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    return render(request, 'rango/cart.html', context=context_dict)

def admin_page(request):
    context_dict = {}
    category_list = Category.objects.all
    context_dict['categories'] = category_list
    return render(request, 'rango/admin_profile.html', context=context_dict)