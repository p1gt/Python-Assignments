from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),	   
    path('addDojo', views.addDojo),
    path('addNinja', views.addNinja)
]