from django import forms
from django.db import models
from django.contrib.auth.models import User
from rango.models import Customer, Category,Product


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ( 'username','email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('address', 'telephone',)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Enter Category Name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Category
        fields = ('name',)

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