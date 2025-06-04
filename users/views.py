from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.db.utils import IntegrityError
from django.contrib.auth import login
from django.core.mail import send_mail
import os


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        try:
            user = form.save()
            login(self.request, user)
            self.send_welcome_email(user.email)
            return super().form_valid(form)

        except IntegrityError:
            form.add_error('email', "Пользователь с таким email уже существует")
            return self.form_invalid(form)

    def send_welcome_email(self, email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        recipient_list = [email]
        send_mail(subject, message, os.getenv("EMAIL_HOST_USER"), recipient_list)


class LoginView(View):
    template_name = 'users/login.html'


class LogoutView(View):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('catalog:product_list')
