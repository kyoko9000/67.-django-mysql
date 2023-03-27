from django.urls import path

from read_text import views

urlpatterns = [
    path('', views.read_text, name='read_text')
]