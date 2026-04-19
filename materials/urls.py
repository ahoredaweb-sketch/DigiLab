from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
    path('download/<int:pk>/', views.download_material, name='download_material'),
]