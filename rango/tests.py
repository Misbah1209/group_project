import os
import re
import json
from rango import forms
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from rango.models import Category,Product,Order
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import base64
#Create a temporary user object#
TEST_IMAGE = '''
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
'''.strip()
#This is referenced from TWD github's progress test but with some modifiations
def creat_user_object():
    user=User.objects.get_or_create(username="testuser",first_name="Test",last_name="User",email="test@test.com")[0]
    user.set_password('123456')
    user.save()

    return user

#This is referenced from TWD github's progress test but with some modifiations
def get_template(path_to_template):

    str=open(path_to_template,'r')
    template_str=""

    for line in str:
        template_str=f"{template_str}{line}"

    str.close()
    return template_str


class LoginTests(TestCase):
    #To check if login is successful
    # This is referenced from TWD github's progress test but with some modifiations

    def test_login_url_exists(self):
        url=""

        try:
            url=reverse(('rango:login'))
        except:
            pass

        self.assertEqual(url,'/rango/login/')

    def test_login_functionality(self):
        test_user_object=creat_user_object()
        response=self.client.post(reverse('rango:login'),{'username':'testuser','password':'123456'})
        try:
            self.assertEqual(test_user_object.id,int(self.client.session['_auth_user_id']),f"2")
        except KeyError:
            self.assertTrue(False)
        self.assertEqual(response.status_code,302,f"3")
        self.assertEqual(response.url,reverse('rango:index'),f"4")

class RegistrationTests(TestCase):
    #To check if the registration is successful
    # This is referenced from TWD github's progress test but with some modifiations

    def test_registration_view_exists(self):
        url=""
        try:
            url=reverse('rango:register')
        except:
            pass
        self.assertEqual(url,'/rango/register/')


    def test_registration_form_creation(self):
        test_user_data={'username':'testuser','password':'123456','email':'test@test.com'}
        test_user_form=forms.UserForm(data=test_user_data)

        self.assertTrue(test_user_form.is_valid())

        test_user=test_user_form.save()
        test_user.set_password(test_user_data['password'])
        test_user.save()

        self.assertEqual(len(User.objects.all()),1)
        self.assertTrue(self.client.login(username='testuser',password='123456'))

    def test_registration_template(self):

        path = os.path.join(settings.TEMPLATE_DIR, 'rango')
        template_path = os.path.join(path, 'register.html')
        self.assertTrue(os.path.exists(template_path),)

        test_str = get_template(template_path)
        block_title_pattern = r'{% block title_block %}(\s*|\n*)Register(\s*|\n*){% (endblock|endblock title_block) %}'

        self.assertTrue(re.search(block_title_pattern, test_str),)

class LogoutTest(TestCase):
    #To check if logout is successful
    # This is referenced from TWD github's progress test but with some modifiations

    def test_good_logout(self):
        test_user_object=creat_user_object()
        self.client.login(username='testuser',password='123456')

        try:
            self.assertEqual(test_user_object.id,int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertTrue(False)

        response=self.client.get(reverse('rango:logout'))
        self.assertEqual(response.status_code,302)
        self.assertEqual(response.url,reverse('rango:index'))
        self.assertTrue('_auth_user_id' not in self.client.session)

class LoginViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        # Test valid login
        response = self.client.post(reverse('rango:login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('rango:index'))

        # Test invalid login
        response = self.client.post(reverse('rango:login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertContains(response, "Invalid login details supplied.")

class CategoryMethodTests(TestCase):
    def test_ensure_category_added(self):
        category = Category(name='test')
        category.save()
        self.assertEqual(category.name, 'test')
    
    def test_category_url_exists(self):
        url=""

        try:
            url=reverse(('rango:add_category'))
        except:
            pass

        self.assertEqual(url,'/rango/add_category/')

    def test_product_url_exists(self):
        url=""

        try:
            url=reverse(('rango:add_product'))
        except:
            pass

        self.assertEqual(url,'/rango/add_product/')

class CategoryShowMethodTests(TestCase):
    # create some item and check the search logic
    def setUp(self):
        # create some items
        c1 = Category(name="category1")
        
        c2 = Category(name="category2")
        c1.save() 
        c2.save()
        image = InMemoryUploadedFile(
            BytesIO(base64.b64decode(TEST_IMAGE)),  # use io.BytesIO
            field_name='tempfile',
            name='tempfile.png',
            content_type='image/png',
            size=len(TEST_IMAGE),
            charset='utf-8',
        )
        p1_c1 = Product(category=c1, title="test_c1_p1", color="Grey", price=3, product_image=image)
        p2_c1 = Product(category=c1, title="test_c1_p2", color="White", price=2, product_image=image)
        p3_c2 = Product(category=c2, title="test_c1_p2", color="White", price=1, product_image=image)
        p1_c1.save()
        p2_c1.save()
        p3_c2.save()


    def test_search_url_exists(self):
        url=""

        try:
            url=reverse('rango:show_category', kwargs={'category_name_slug': "category1"})
        except:
            pass

        self.assertEqual(url,'/rango/category/category1/')

    def test_search_no_exists_data(self):
        # to check with empty data

        url = reverse('rango:show_category', kwargs={'category_name_slug': "category2"})
        response = self.client.get(url, data={"keyword": "123213123123213tttttitle"})

        response = response.context[0]
        self.assertEqual(response["products"].count(), 0)

        response = self.client.get(url, data={"color": "brown"})
        response = response.context[0]
        self.assertEqual(response["products"].count(), 0)

    def test_search_category_data(self):
        # to check search with category data
        url = reverse('rango:show_category', kwargs={'category_name_slug': "category1"})
        response = self.client.get(url)
        response = response.context[0]
        self.assertEqual(response["category"].name, "category1")
        url = reverse('rango:show_category', kwargs={'category_name_slug': "category2"})
        response = self.client.get(url)
        response = response.context[0]
        self.assertEqual(response["category"].name, "category2")
    #
    def test_search_products_data(self):
        # to check search with product data
        url = reverse('rango:show_category', kwargs={'category_name_slug': "category1"})
        response = self.client.get(url, data={"keyword": "test_c1_p1"})
        response = response.context[0]

        self.assertEqual(len(response["products"]), 1)
        self.assertEqual(response["products"][0].title, "test_c1_p1")

    def test_search_products_order(self):
        # to to check search by price order
        url = reverse('rango:show_category', kwargs={'category_name_slug': "category1"})
        response = self.client.get(url, data={"sort": "sx"})
        response = response.context[0]

        self.assertEqual(len(response["products"]), 2)
        self.assertEqual(int(response["products"][0].price), 2)

        response = self.client.get(url, data={"sort": "jx"})
        response = response.context[0]
        self.assertEqual(len(response["products"]), 2)
        self.assertEqual(int(response["products"][0].price), 3)

    def test_search_products_color(self):
        # to check search by color
        url = reverse('rango:show_category', kwargs={'category_name_slug': "category1"})
        response = self.client.get(url, data={"color": "white"})
        response = response.context[0]

        self.assertEqual(len(response["products"]), 1)
        self.assertEqual(response["products"][0].color, "White")


class CheckOutTestCase(TestCase):
    def test_cart_view_exists(self):
        url = ""
        try:
            url = reverse('rango:cart')
        except:
            pass
        self.assertEqual(url, '/rango/cart/')

    def test_checkout_save(self):
        test_order_data = {'quantity': 6, 'billAmt': 666}
        test_order_form = forms.OrderForm(data=test_order_data)

        self.assertTrue(test_order_form.is_valid())

        test_order = test_order_form.save()
        # test_order.set_password(test_user_data['password'])
        test_order.save()

        order = Order.objects.get(quantity=6)
        self.assertTrue(order is not None)
        self.assertEqual(order.billAmt, 666)


    def test_checkout_api(self):
        response = self.client.post(reverse('rango:cart'), {'quantity': 7, 'billAmt': 777})

        self.assertEqual(response.status_code, 302)
        order = Order.objects.get(quantity=7)
        self.assertTrue(order is not None)
        self.assertEqual(order.billAmt, 777)