from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def listnews(request):
    return render(request, 'main/listnews.html')


def addnews(request):
    return render(request, 'main/addnews.html')

def authorisation(request):
    return render(request, 'main/authorisation.html')
