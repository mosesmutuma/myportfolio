from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.about, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact_view, name='contact'),
]
