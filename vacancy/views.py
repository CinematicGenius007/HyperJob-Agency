from django.shortcuts import render, redirect
from .models import Vacancy, VacancyForm
from django.http import HttpResponseForbidden, HttpResponseNotFound


def vacancies(request):
    """ A view to return the vacancy page """
    context = {
        'title': 'Vacancy',
        'vacancies': Vacancy.objects.all(),
    }
    return render(request, 'vacancy/vacancy.html', context)


def create_vacancy(request):
    """ A view to return the vacancy page """
    if request.method == 'POST':
        if request.user.is_authenticated and request.user.is_staff:
            form = VacancyForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
            return redirect('/')
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseNotFound()