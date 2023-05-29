from django.urls import path     
from . import views
urlpatterns = [
    path('', views.red),
    path('time_display', views.index)
]