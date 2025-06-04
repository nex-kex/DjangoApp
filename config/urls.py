from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls", namespace="blog")),
path("users/", include("users.urls", namespace="users")),
    path("", include("catalog.urls", namespace="catalog")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
