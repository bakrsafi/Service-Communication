from django.shortcuts import render

from django.http import JsonResponse
from .product_api import get_all_products, update_product, get_product, add_product


def sync_products(request):
    products = get_all_products()
    return JsonResponse({"products": products})

def sync_products_id(request,pk):
    products = get_product(pk)
    return JsonResponse({"products": products})


def update_sample_product(request):
    status, data = update_product(product_id=1, data={"price": 55.99})
    return JsonResponse({"status": status, "data": data})


new_product = {
    "name": "Wireless Mouse",
    "description": "Ergonomic wireless mouse",
    "price": "29.99",
    "stock": 50,
    "categories": [1],  
    "detail": {
        "manufacturer": "Logitech",
        "warranty_period": 24
    }
}

def creat_sample_product(request):
    added_product = add_product(new_product)
    print(added_product)
    return JsonResponse({"status": 200, "data": added_product})






