from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skill/', views.skill, name='skill'),
    path('contact/', views.contact, name='contact'),
    # path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('download-pdf/', views.my_view, name='download_pdf'),
    
]
