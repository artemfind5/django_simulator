from django.urls import path

from untitled.calc import views


urlpatterns = [
    path('', views.index),
]