from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Home"),
    path('about',views.about,name="about"),
    #path('contact',views.contact,name="contact"),
    path('contact',views.contact,name="contact"),
    path('service',views.service,name="service"),
    path('gallery',views.gallery,name="gallery"),
    path('product',views.product,name="product"),
]