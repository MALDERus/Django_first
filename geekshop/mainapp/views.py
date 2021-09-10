from django.shortcuts import render
from mainapp.models import Product

# Create your views here.

def main(request):
    title = 'магазин'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request):
    context = {
        'title': 'каталог'
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contact.html', context)

def temp(request):
    return render(request, 'mainapp/temp1.html', {'data': 10})