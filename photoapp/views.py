from django.shortcuts import render
from .models import Photo, Category
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PhotoForm


# def home(request):
#     photos = Photo.objects.all()
#     categories = Category.objects.all()

#     context = {
#         "photos": photos,
#         "categories": categories
#     }
#     return render(request, 'photoapp/home.html', context)


class HomePageView(ListView):
    model = Photo
    template_name = "photoapp/home.html"


class CreatePhotoView(CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = "photoapp/upload.html"
    success_url = reverse_lazy('home')


def about(request):
    return render(request, 'photoapp/about.html')


def contact(request):
    return render(request, 'photoapp/contact.html')
