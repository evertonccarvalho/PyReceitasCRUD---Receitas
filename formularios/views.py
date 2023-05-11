from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'eanforms/pages/home.html')


def recipe(request, id):
    return render(request, 'eanforms/pages/recipe-view.html')


def obitos(request):
    return render(request, 'eanforms/master/obitos.html')


def dashboard(request):
    return render(request, 'eanforms/master/dashboard.html')
