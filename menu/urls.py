from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.MyLoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('signup', views.MySignupView.as_view()),
    path('home', views.home, name='home'),
]
