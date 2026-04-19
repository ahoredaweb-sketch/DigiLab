from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from django.db.models import Q
from django.http import FileResponse


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


from django.db.models import F
from django.shortcuts import get_object_or_404, redirect

def download_material(request, pk):
    material = get_object_or_404(Material, pk=pk)

    # ✅ safe counter increment (IMPORTANT)
    Material.objects.filter(pk=pk).update(downloads=F('downloads') + 1)

    # ✅ redirect to file
    return redirect(material.file.url)