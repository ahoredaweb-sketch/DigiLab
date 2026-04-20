from django.urls import path
from . import views
from django.shortcuts import get_object_or_404, redirect
from .models import Material

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
    path('download/<int:id>/', views.download, name='download'),
]

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from .models import Material

def download(request, id):
    material = get_object_or_404(Material, id=id)

    if not material.file:
        return HttpResponse("File not found", status=404)

    material.downloads += 1
    material.save()

    return redirect(material.file.url)