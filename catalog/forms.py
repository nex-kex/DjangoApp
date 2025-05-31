from django import forms
from django.core.exceptions import ValidationError

from .mixins import FormControlMixin
from .models import Product


class ProductForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        excluded_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "дёшево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        for word in excluded_words:
            if word in name.lower() or word in description.lower():
                raise ValidationError(
                    'Слово "%(word)s" не должно содержаться в названии или описании продукта.',
                    params={"word": word},
                )
