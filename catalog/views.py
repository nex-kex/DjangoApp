from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

from .forms import ProductForm
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = "catalog.add_product"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", args=[self.object.pk])


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.change_product"):
            return ProductForm
        raise PermissionDenied

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm("catalog.delete_product"):
            return ProductForm
        raise PermissionDenied


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_unpublish_product"

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs["pk"])

        product.status = False
        product.save()

        return redirect("catalog:product_list")


class ProductPublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = "catalog.can_publish_product"

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs["pk"])

        product.status = True
        product.save()

        return redirect("catalog:product_list")
