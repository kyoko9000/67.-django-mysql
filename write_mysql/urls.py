from django.urls import path

from write_mysql import views

urlpatterns = {
    path('', views.signin, name='signin'),
}