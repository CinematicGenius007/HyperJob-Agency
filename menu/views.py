from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from resume.models import ResumeForm
from vacancy.models import VacancyForm


def index(request):
    return render(request, 'menu/index.html')


def home(request):
    context = {
        'is_staff': request.user.is_authenticated and request.user.is_staff,
        'resume_form': ResumeForm(),
        'vacancy_form': VacancyForm(),
        'resume_redirect': '/resume/new',
        'vacancy_redirect': '/vacancy/new',
        'title': 'Home'
    }
    return render(request, 'menu/home.html', context)


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True  
    template_name = 'menu/login.html'
