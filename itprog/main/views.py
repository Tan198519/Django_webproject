from django.shortcuts import render


# Create your views here.

def index(request):
    data = {
        'value': ['Customer', 'Apartments', 'Influencers'],
        'obj': {'car': 'bmw',
                'age': '21',
                'hobby': 'swim'
                }
    }
    return render(request, 'main/index.html', data)


def login(request):
    return render(request, 'main/login.html')


def data_schemas(request):
    return render(request, 'main/data_schemas.html')
