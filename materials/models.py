from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
    title = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title