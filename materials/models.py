from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.http import HttpResponse
from .models import Material


class Material(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    course = models.CharField(max_length=100, db_index=True)

    # 🔥 FIXED: Cloudinary file storage
    file = CloudinaryField(resource_type='raw')

    # 🔥 SINGLE download counter (no duplicates)
    downloads = models.PositiveIntegerField(default=0)

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course})"
    
def delete_all_materials(request):
    Material.objects.all().delete()
    return HttpResponse("All materials deleted successfully")