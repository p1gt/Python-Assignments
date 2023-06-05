from django.shortcuts import render, HttpResponse, redirect
from . import models

def root(request):
    data = {
        'dojoInfo': models.get_all_dojos(),
        'ninjaInfo' :models.get_all_ninja()
      }
    return render(request,'root.html', data)

def addDojo(request):
    models.addDojo(request)
    return redirect('/')
    
def addNinja(request):
    models.addNinja(request)
    return redirect('/')    