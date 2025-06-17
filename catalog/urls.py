from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("", views.ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("create", views.ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/",views.ProductUpdateView.as_view(),name="product_update"),
    path("<int:pk>/delete/",views.ProductDeleteView.as_view(),name="product_delete"),
    path("<int:pk>/unpublish/",views.ProductUnpublishView.as_view(),name="product_unpublish"),
]
