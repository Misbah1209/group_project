from django.contrib import admin
from rango.models import Category, Product,Order,Customer

# Register your models here.

# Add in this classes to customise the Admin Interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class OrderAdmin(admin.ModelAdmin):
    pass

# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)