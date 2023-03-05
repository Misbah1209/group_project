import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Product

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views':1},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views':2},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views':3} ]
    
    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views':4},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/','views':5},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/','views':6} ]
    
    other_pages = [
        {'title':'Bottle','url':'http://bottlepy.org/docs/dev/','views':7},
        {'title':'Flask', 'url':'http://flask.pocoo.org','views':8} ]
    
    cats = {'Python': {'pages': python_pages, 'views': 128, "likes": 64},
        'Django': {'pages': django_pages, "views" : 64, "likes": 32},
        'Other Frameworks': {'pages': other_pages, "views": 32, "likes": 16} }
  
    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for p in cat_data['products']:
            add_page(c,p['title'],p['product_image'],p['price'],p['color'])

    for c in Category.objects.all():
        for p in Product.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_product(cat, title, product_image, price,color):
    p = Product.objects.get_or_create(category=cat, title=title)[0]
    p.product_image=product_image
    p.price=price
    p.color=color
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()