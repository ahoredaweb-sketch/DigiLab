from django.shortcuts import render, redirect, get_object_or_404
from .models import Material
from django.http import HttpResponse


# ✅ HOME VIEW
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


# ✅ UPLOAD VIEW (Cloudinary-safe)
def upload_material(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        course = request.POST.get('course')
        file = request.FILES.get('file')

        if not file:
            return render(request, 'materials/upload.html', {
                'error': 'No file selected'
            })

        try:
            Material.objects.create(
                title=title,
                course=course,
                file=file,
                uploaded_by=request.user if request.user.is_authenticated else None
            )
        except Exception as e:
            return HttpResponse(f"Upload error: {str(e)}")

        return redirect('home')

    return render(request, 'materials/upload.html')


# ✅ DOWNLOAD (CORRECT FOR CLOUDINARY)
def download(request, id):
    material = get_object_or_404(Material, id=id)

    material.downloads += 1
    material.save()

    return redirect(material.file.url)


# ✅ DELETE (ADMIN LATER)
def delete_material(request, id):
    material = get_object_or_404(Material, id=id)
    material.delete()
    return redirect('home')