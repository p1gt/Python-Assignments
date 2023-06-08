from django.shortcuts import render, redirect
from . import models
from .models import Shows
def root(request):
    return redirect('/shows')

def shows(request):
    shows = models.Shows.objects.all()
    return render(request, 'shows.html', {'shows': shows})

def new(request):
    return render(request, 'new.html')

def create(request):
    models.create(request)
    new_show = models.create(request)
    return redirect(f'/shows/{new_show.id}')

def showID(request, id):
    show = Shows.objects.get(id=id)
    return render(request, 'id.html', {'show': show})

def edit(request, id):
    show = Shows.objects.get(id=id)
    return render(request, 'edit.html', {'show': show})

def update(request, id):
    if request.method == 'POST':
        show = Shows.objects.get(id=id)
        show.title = request.POST.get('title')
        show.network = request.POST.get('network')
        show.release_date = request.POST.get('release_date')
        show.desc = request.POST.get('desc')
        show.save()
        return redirect(f'/shows/{id}')

def destroy(request, id):
    show = Shows.objects.get(id=id)
    show.delete()
    return redirect('/')