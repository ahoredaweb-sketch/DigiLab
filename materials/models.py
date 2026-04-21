from django.db import models
from django.contrib.auth.models import User


class Material(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    course = models.CharField(max_length=100, db_index=True)
    file = models.FileField(upload_to='materials/')

    downloads = models.PositiveIntegerField(default=0)

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    download_count = models.PositiveIntegerField(default=0)  # 🔥 renamed for clarity
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course})"