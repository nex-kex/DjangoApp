from django.urls import path

from catalog.apps import CatalogConfig

from . import views
from .services import CategoryProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("create", views.ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="product_update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="product_delete"),
    path("<int:pk>/unpublish/", views.ProductUnpublishView.as_view(), name="product_unpublish"),
    path("<int:pk>/publish/", views.ProductPublishView.as_view(), name="product_publish"),
    path("category_list/", views.CategoryListView.as_view(), name="category_list"),
    path("category_products_list/<int:pk>/", CategoryProductsListView.as_view(), name="category_products_list"),
]
