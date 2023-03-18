import os
import re
from rango import forms
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from rango.models import Category,Product,Order

#Create a temporary user object#

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

class OrderMethodTests(TestCase):
    def test_ensure_order_saved(self):
        order = Order(quantity=1,billAmt=50.00)
        order.save()
        self.assertEqual(order.quantity, 1)

    def test_cart_url_exists(self):
        url=""

        try:
            url=reverse(('rango:cart'))
        except:
            pass

        self.assertEqual(url,'/rango/cart/')