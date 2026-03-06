from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Product


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.object.all()
    cart: list = request.session.get('cart', [])
    return render(request, 'shop/product_list.html',
                  context={'products': products, ' cart_count': len(cart), })


def add_to_cart(request: HttpRequest) -> JsonResponse:
    product_id = request.POST.get('product_id')
    cart: list = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)
        cart = request.session.get('cart')

    return JsonResponse({'status': 'ok', 'cart_count': len(cart)})


def remove_from_cart(request: HttpRequest) -> JsonResponse:
    product_id = request.POST.get('product_id')
    cart: list = request.session.get('cart', [])

    if product_id in cart:
        cart.remove(product_id)
        cart = request.session.get('cart')
    return JsonResponse({'status': 'ok', 'cart_count': len(cart)})
