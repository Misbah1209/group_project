import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'group_project.settings')

import django
django.setup()
from rango.models import Category, Product

def populate():
    dining_products = [
        {'title': 'Velvet Chair',
        'product_image':'product_image/chair1.jpg',
        'price':120.00,
        'color':'Green'},
        {'title': 'Oakley Set of 2',
        'product_image':'product_image/chair2.jpg',
        'price':90.00,
        'color':'Orange'},
        {'title': 'Dining Bench',
        'product_image':'product_image/chair3.jpg',
        'price':75.50,
        'color':'White'}, 
        {'title': 'Ceramic Dining Table',
        'product_image':'product_image/table1.jpg',
        'price':140.00,
        'color':'Black'},
        {'title': 'Rectangle Table',
        'product_image':'product_image/table2.jpg',
        'price':105.00,
        'color':'White'},
        {'title': 'Wooden Table',
        'product_image':'product_image/table3.jpg',
        'price':155.50,
        'color':'Brown'}, ]
    
    lounge_products = [
       {'title': 'L Sofa',
        'product_image':'product_image/sofa1.jpg',
        'price':120.00,
        'color':'Green'},
        {'title': 'Chesterfeild Sofa',
        'product_image':'product_image/sofa2.jpg',
        'price':90.00,
        'color':'Blue'},
        {'title': 'Grid Arched Mirror',
        'product_image':'product_image/mirror1.jpg',
        'price':75.50,
        'color':'Black'}, 
        {'title': 'Irregular Frameless Mirror',
        'product_image':'product_image/mirror2.jpg',
        'price':140.00,
        'color':'White'},
        {'title': 'Wooven Cabinet',
        'product_image':'product_image/cabin1.jpg',
        'price':105.00,
        'color':'Black'},
        {'title': 'Rattan Cabinet',
        'product_image':'product_image/cabin2.jpg',
        'price':155.50,
        'color':'Brown'}, ]
    
    bedroom_products = [
        {'title': 'Wooden Solid Bed',
        'product_image':'product_image/bed1.jpg',
        'price':120.00,
        'color':'White'},
        {'title': 'Velvet Framed Bed',
        'product_image':'product_image/bed2.jpg',
        'price':190.00,
        'color':'Blue'},
        {'title': 'Gretel House Bed',
        'product_image':'product_image/kid1.jpg',
        'price':75.50,
        'color':'White'}, 
        {'title': 'High Solid Bed',
        'product_image':'product_image/kid2.jpg',
        'price':140.00,
        'color':'Brown'},
        {'title': 'Wooven Framed Wardrobe',
        'product_image':'product_image/wardrobe1.jpg',
        'price':105.00,
        'color':'Black'},
        {'title': 'Rattan Wardrobe',
        'product_image':'product_image/wardrobe2.jpg',
        'price':155.50,
        'color':'Brown'}, ]
    
    garden_products = [
        {'title': 'Bar Trolley',
        'product_image':'product_image/trolley1.jpg',
        'price':120.00,
        'color':'Gold'},
        {'title': 'Konya 2 Seater',
        'product_image':'product_image/outchair1.jpg',
        'price':90.00,
        'color':'Black'},
        {'title': 'Cacoon Chair',
        'product_image':'product_image/outchair2.jpg',
        'price':75.50,
        'color':'White'}, 
        {'title': 'Bar Stool',
        'product_image':'product_image/trolley2.jpg',
        'price':140.00,
        'color':'Gold'},
        {'title': 'Grey Gazebo',
        'product_image':'product_image/outchair3.jpg',
        'price':405.00,
        'color':'Grey'},
        {'title': 'Pet Basket',
        'product_image':'product_image/pet2.jpg',
        'price':105.50,
        'color':'Black'}, ]

    cats = {'Dining': {'products': dining_products},
            'Lounge': {'products': lounge_products},
            'Bedroom': {'products': bedroom_products},
            'Garden': {'products': garden_products} 
            }
  
    for cat, cat_data in cats.items():
        c= add_cat(cat)
        for p in cat_data['products']:
            add_product(c,p['title'],p['product_image'],p['price'],p['color'])

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