from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category
from .cart import Cart

def category_detail(request, slug):
    
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    
    context = {
        'category': category,
        'products': products,
    }
    
    return render(request, 'store/category_detail.html', context)

def search(request):
    query = request.GET.get('query', '')
    
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'store/search.html', {
        'query': query,
        'products': products,
    })


def product_detail(request, category_slug, slug):
    
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    
    context = {
        'product': product,
    }
    
    return render(request, 'store/product_detail.html', context)

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    
    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    
    return render(request, 'store/cart_view.html', {
        'cart': cart
    })

def change_quantity(request, product_id):
    action = request.GET.get('action', '')
    
    if action:
        quantity = 1
        
        if action == 'decrease':
            quantity = -1
            
        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    return redirect('cart_view')