from django.urls import path

from HTML import views

urlpatterns = [
    path('', views.HTML, name='HTML')
]
