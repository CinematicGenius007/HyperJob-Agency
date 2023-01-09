from django.shortcuts import render, redirect
from .models import Resume, ResumeForm
from django.http import HttpResponseForbidden, HttpResponseNotFound


def resumes(request):
    """ A view to return the resume page """
    context = {
        'title': 'Resume',
        'resumes': Resume.objects.all(),
    }
    return render(request, 'resume/resume.html', context)


def create_resume(request):
    """ A view to return the resume page """
    if request.method == 'POST':
        if request.user.is_authenticated and not request.user.is_staff:
            form = ResumeForm(request.POST)
            """Adding the user to the form"""
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
            return redirect('/')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotFound()