from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Product
def index(request):
    return render(request, 'index.html', {'page-title' : 'shop'})

def products_view(request):
    products = Product.objects.all()
    context = {
        'products' : products,
    }
    return render(request, 'products.html', context)