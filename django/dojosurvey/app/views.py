from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        language = request.POST.get('language')
        comment = request.POST.get('comment')
        context = {'name': name,
                   'language': language,
                   'city': city,
                   'comment': comment}
        return render(request, 'result.html', context)