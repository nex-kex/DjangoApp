from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')


class LoginView(View):
    form_class = CustomUserCreationForm
    template_name = 'users/login.html'


class LogoutView(View):
    form_class = CustomUserCreationForm
    template_name = 'users/logout.html'
    next_page = reverse_lazy('catalog:product_list')
