from django.shortcuts import render, redirect, get_object_or_404    
from .models import Product, CartItem


def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })
    
def remove_from_cart(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect('cart')


def update_cart(request, id, action):
    item = get_object_or_404(CartItem, id=id)

    if action == 'increase':
        item.quantity += 1
        item.save()

    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()

    return redirect('cart')
