from django.contrib import admin
from django.urls import path
from rango import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
    path('', views.index, name='index'),
]
