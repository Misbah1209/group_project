from django import forms
from django.db import models
from django.contrib.auth.models import User
from rango.models import Customer, Category,Product,Order

# This is referenced from TWD chapter 9, but modifications have been made.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ( 'username','email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'telephone',)


#this is the category form used by admin to add new category
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Enter Category Name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Category
        fields = ('name',)

#this is the product form used by admin to add new products
class ProductForm(forms.ModelForm):

    class Meta:
        model= Product
        fields=['category','title','product_image','price','color']
        label = {
                'title': ('Product Name'),
                'price': ('Product Price'),
                'color': ('Product Color'),
                'product_image': ('Product Image'),
            }
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

#this is the order form used by user to perform checkout
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['quantity','billAmt']
        label = {
                'quantity': ('quantity'),
                'billAmt': ('billAmt'),
            }
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data