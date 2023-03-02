from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    img = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
