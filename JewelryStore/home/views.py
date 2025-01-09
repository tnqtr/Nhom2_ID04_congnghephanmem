from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request):
    return render(request, 'home/home.html')
def loginUser(request):
    return render(request, 'home/login.html')

