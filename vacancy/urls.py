from django.urls import path
from . import views

urlpatterns = [
    path('vacancies', views.vacancies, name='vacancy'),
    path('vacancy/new', views.create_vacancy, name='create_vacancy'),
]