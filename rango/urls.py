from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
