from django.shortcuts import render

# Create your views here.

def main(request):
    context = {
        'title': 'магазин'
    }
    return render(request, 'mainapp/index.html', context)

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