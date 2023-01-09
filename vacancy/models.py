from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Vacancy(models.Model):
    description = models.TextField(max_length=1024)
    author = models.OneToOneField(User, on_delete=models.CASCADE)


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['description']
