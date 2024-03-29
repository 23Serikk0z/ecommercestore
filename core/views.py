from django.shortcuts import render
from store.models import Product



def index(request):
    
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]
    
    context = {
        'products': products 
    }
    
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')
