from django.shortcuts import render, redirect
import random

def root(request):
    return redirect('/gold')

def index(request):
    counter = request.session.get('counter', 0)
    history = request.session.get('history', [])
    counter0 = random.randint(10, 20)
    counter1 = random.randint(-50, 50)
    data = {
        'counter': counter,
        'counter0': counter0,
        'counter1': counter1,
        'history': history
    }
    return render(request, 'index.html', data)

def process(request):
    if request.method == 'POST':
        gold = request.POST.get('gold')
        counter = request.session.get('counter', 0)
        history = request.session.get('history', [])
        if gold in ['farm', 'cave', 'house']:
            counter_change = random.randint(10, 20)
            counter += counter_change
            history.append(counter_change)
        elif gold == 'quest':
            counter_change = random.randint(-50, 50)
            counter += counter_change
            history.append(counter_change)
        request.session['counter'] = counter
        request.session['history'] = history
    return redirect('/gold')