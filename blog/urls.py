from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("<int:pk>/", views.PostDetailView.as_view(), name='post_detail'),
    path("post_list/", views.PostListView.as_view(), name='post_list'),
    path("create/", views.PostCreateView.as_view(), name='post_create'),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name='post_update'),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name='post_delete'),
]
