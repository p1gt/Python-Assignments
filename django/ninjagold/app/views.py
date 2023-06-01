from django.shortcuts import render, redirect

def enter(request):
    return redirect('/gold')
def index(request):
    return render(request, 'index.html')