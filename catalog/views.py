from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .models import Product


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])


class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "image", "category", "price")
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
