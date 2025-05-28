from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    text = models.TextField(
        verbose_name="Содержимое"
    )
    image = models.ImageField(
        upload_to="blog/media/",
        null=True,
        blank=True,
        verbose_name="Превью"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публикации"
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["created_at", "views_count"]
