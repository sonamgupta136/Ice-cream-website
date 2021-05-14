from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("clients", views.clients, name='clients'),
    path("softy",views.softy, name='softy'),
    path("familypack",views.familypack, name='familypack'),


    path("contact", views.contact, name='contact'),

]