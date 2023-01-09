from django.urls import path
from . import views

urlpatterns = [
    path('resumes', views.resumes, name='resumes'),
    path('resume/new', views.create_resume, name='create_resume'),
]
