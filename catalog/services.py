from django.core.cache import cache
from django.views.generic import ListView

from .models import Product


class CategoryProductsListView(ListView):
    model = Product
    template_name = "product_list.html"

    def get_queryset(self):
        category_id = self.kwargs.get("pk")
        key = f"category_{category_id}_queryset"

        queryset = cache.get(key)

        if not queryset:
            queryset = super().get_queryset().filter(category_id=category_id)
            cache.set(key, queryset, 60 * 15)

        return queryset
