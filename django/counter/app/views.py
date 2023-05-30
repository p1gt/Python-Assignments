from django.shortcuts import render, redirect

def index(request):
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1
    data = {
        "visits" : request.session['visits']
    }
    return render(request, 'index.html', data)
def destroy(request):
    del request.session['visits']
    return redirect('/')