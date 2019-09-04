from django.contrib import admin
from django.urls import include, path, re_path

from .views import *

urlpatterns = [
    #shop urls
    path('', index, name='index'),
    path('products/', products_view, name='products_view'),
]
