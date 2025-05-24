from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test data to the database'

    def handle(self, *args, **kwargs):

        # Удаление данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Добавление тестовых данных
        category, _ = Category.objects.get_or_create(name='Процессоры')

        products = [
            {
                "name": "AMD Ryzen 5 7500F OEM",
                "description": "AM5, 6 x 3.7 ГГц, L2 - 6 МБ, L3 - 32 МБ, 2 х DDR5-5200 МГц, TDP 65 Вт",
                "image": "",
                "category": category,
                "price": 13799,
                "created_at": "2025-05-24",
                "updated_at": "2025-05-24",
            },
            {
                "name": "AMD Ryzen 7 7800X3D OEM",
                "description": "AM5, 8 x 4,2 ГГц, L2 - 8 МБ, L3 - 96 МБ, 2 х DDR5-5200 МГц, AMD Radeon Graphics, TDP 120 Вт",
                "image": "",
                "category": category,
                "price": 37799,
                "created_at": "2025-05-24",
                "updated_at": "2025-05-24",
            }
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}.'))
            else:
                self.stdout.write(self.style.WARNING(f'Product "{product.name}" already exists.'))

