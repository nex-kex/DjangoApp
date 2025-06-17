from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser


class UserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("first_name", "last_name", "phone_number", "country", "avatar")


class CustomUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False, help_text="Изображение. Необязательное поле.")
    phone_number = forms.CharField(max_length=15, required=False, help_text="Номер телефона. Необязательное поле.")
    country = forms.CharField(max_length=50, required=False, help_text="Страна. Необязательное поле.")
    usable_password = None

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "first_name", "last_name", "phone_number", "country", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'].lower()
        user.username = user.email
        if commit:
            user.save()
        return user

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number
