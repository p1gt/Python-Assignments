from django.shortcuts import render, redirect
from . import models
from .models import Shows
from django.contrib import messages

def root(request):
    return redirect('/shows')

def shows(request):
    data = {
        'shows': models.Shows.objects.all()
    }
    return render(request, 'shows.html',data)

def new(request):
    return render(request, 'new.html')

def create(request):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/shows/new')
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        Shows.objects.create(title=title, network=network, release_date=release_date, desc=desc)
    return redirect('/')

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