from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def home(request):
    context = {
        "products": Product.objects.all()
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # phone = request.POST.get("phone")
        # message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "catalog/contacts.html")


def product_details(request, product_id):
    context = {
        "product": Product.objects.get(id=product_id)
    }
    return render(request, 'catalog/product_details.html', context)
