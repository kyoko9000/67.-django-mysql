from django.urls import path

from phu import views

urlpatterns = [
    path('', views.index, name="ii")
]