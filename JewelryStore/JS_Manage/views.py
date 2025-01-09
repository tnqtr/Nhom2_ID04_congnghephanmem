from django.shortcuts import render

from django.http import HttpResponse

def hoaDon(request):
    return HttpResponse("Hello world!")
def nhanVien(request):
    return HttpResponse("Hello world!")
def home(request):
    return render(request, 'home.html')