from django.contrib import admin
from django.urls import path, include
from starter import views

urlpatterns = [
    path('', include('starter.urls')),
    path('admin/', admin.site.urls),
]
