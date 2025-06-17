from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig

from . import views

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page="catalog:product_list"), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path("<int:pk>/", views.UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name="user_update"),
]
