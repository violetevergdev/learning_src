from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values': [
            'Some', 'Pump', "warm"
        ],
        'obj': {
            'car': 'BMW',
            'age': 18
        }
    }

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')