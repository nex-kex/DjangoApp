# Generated by Django 5.2.1 on 2025-05-28 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Содержимое")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="blog/media/",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "is_published",
                    models.BooleanField(default=False, verbose_name="Признак публикации"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(default=0, verbose_name="Количество просмотров"),
                ),
            ],
            options={
                "verbose_name": "Блоговая запись",
                "verbose_name_plural": "Блоговые записи",
                "ordering": ["created_at", "views_count"],
            },
        ),
    ]
