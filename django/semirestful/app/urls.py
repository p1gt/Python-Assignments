from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:id>', views.showID),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<id>/update', views.update),
    path('shows/<int:id>/destroy', views.destroy),
]
