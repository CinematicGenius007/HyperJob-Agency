from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Resume(models.Model):
    description = models.TextField(max_length=1024)
    author = models.OneToOneField(User, on_delete=models.CASCADE)


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description']
