from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rango import views
app_name = 'rango'

# below are the url paths for the application

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('admin/', views.admin_page, name='admin'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_product/', views.add_product, name='add_product'),
    path('register_completed',views.register_completed,name="register_completed"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
