from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from django.db.models import Q
from django.http import FileResponse

from django.shortcuts import get_object_or_404, redirect
from django.http import FileResponse, Http404
from django.db.models import F
import requests

def home(request):
    title_query = request.GET.get('q')
    course_query = request.GET.get('course')

    materials = Material.objects.all()

    if title_query:
        materials = materials.filter(title__icontains=title_query)

    if course_query:
        materials = materials.filter(course__icontains=course_query)

    materials = materials.order_by('-id')

    return render(request, 'materials/home.html', {
        'materials': materials
    })


def upload_material(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        course = request.POST.get('course')
        file = request.FILES.get('file')

        if not file:
            return render(request, 'materials/upload.html', {
                'error': 'No file selected'
            })

        Material.objects.create(
            title=title,
            course=course,
            file=file,
            uploaded_by=None
        )

        return redirect('home')

    return render(request, 'materials/upload.html')


def download_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    material.downloads += 1
    material.save()

    file_url = material.file.url

    response = requests.get(file_url, stream=True)

    if response.status_code != 200:
        raise Http404("File not found")

    return FileResponse(
        response.raw,
        as_attachment=True,
        filename=material.file.name.split('/')[-1]
    )