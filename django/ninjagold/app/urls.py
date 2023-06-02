from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('gold', views.index),
    path('process', views.process),
]