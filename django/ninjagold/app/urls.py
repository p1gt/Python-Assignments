from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter),
    path('gold', views.index),
]