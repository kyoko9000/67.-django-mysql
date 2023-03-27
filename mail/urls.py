from django.urls import path

from mail import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
]