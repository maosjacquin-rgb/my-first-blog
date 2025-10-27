from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)     # 🔹 Fecha de creación (no cambia)
    updated_date = models.DateTimeField(auto_now=True)         # 🔹 Fecha de última edición
    published_date = models.DateTimeField(blank=True, null=True)  # 🔹 Fecha de publicación manual

    def publish(self):
        if not self.published_date:                            # Solo se asigna si no tenía fecha
            self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title