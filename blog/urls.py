from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post_list_all/", views.PostListViewAll.as_view(), name="post_list_all"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/publish/", views.PublishPost.as_view(), name="publish"),
]
