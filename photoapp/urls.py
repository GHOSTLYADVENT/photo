from django.urls import path
from . import views  # function based views
from .views import HomePageView, CreatePhotoView  # class based views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('upload/', CreatePhotoView.as_view(), name='upload'),
]
