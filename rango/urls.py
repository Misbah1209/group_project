from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rango import views
app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    # path('product/',views.show_category, name='show_category'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('admin/', views.admin_page, name='admin_page'),
    path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
