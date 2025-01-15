from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request, 'home/home.html')
def index (request):
    return render(request, 'home/pages/index.html')
def index2 (request):
    return render(request, 'home/pages/index2.html')
def index3 (request):
    return render(request, 'home/pages/index3.html')
def cards(request):
    return render(request, 'home/pages/widgets/cards.html')
