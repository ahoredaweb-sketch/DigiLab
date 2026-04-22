from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_material, name='upload'),
    path('download/<int:id>/', views.download, name='download'),
    path('delete/<int:id>/', views.delete_material, name='delete'),
]