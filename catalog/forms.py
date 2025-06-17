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

    def clean_name(self):
        name = self.cleaned_data.get("name")

        for word in self.excluded_words:
            if word in name.lower():
                raise ValidationError(
                    'Слово "%(word)s" не должно содержаться в названии продукта.',
                    params={"word": word},
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")

        for word in self.excluded_words:
            if word in description.lower():
                raise ValidationError(
                    'Слово "%(word)s" не должно содержаться в описании продукта.',
                    params={"word": word},
                )

        return  description

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной.")

        return price