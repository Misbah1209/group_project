from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
    color = models.CharField(max_length=128)
    
    def __str__(self):
        return self.title

class Order(models.Model):
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    billAmt = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.Order


class Customer(models.Model):
    # The User model has five attributes: 
    #username,password,email address,first name and the user’s surname.
    
    # This line is required. Links customer to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The additional attributes we wish to include.
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20,null=False)
    
    def __str__(self):
        return self.user.username