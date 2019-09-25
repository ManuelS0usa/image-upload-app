from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import ImageForm
from .models import Image



def Home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def delete_image(request, pk):
    if request.method == 'POST':
        image = Image.objects.get(pk=pk)
        image.delete()
    return redirect('home')

