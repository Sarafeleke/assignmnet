from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import home,about_Us,Blog,services,Contact_us
urlpatterns = [
   
   path('',home,name="home_url"),
   path('about/',about_Us,name="about_Us_url"),
   path('services/',services,name="services_url"),
   path('contact/',Contact_us,name="Contact_Us_url")]