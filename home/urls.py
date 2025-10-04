from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("Services/webdev", views.webdev, name='webdev'),
    path("Services/mobileapp", views.mobileapp, name='mobileapp'),
    path("Services/design", views.design, name='design'),
    path('project/<int:project_id>/pay/', views.start_payment, name='start_payment'),
    path('project/<int:project_id>/download/', views.download_pdf, name='download_pdf'),
]