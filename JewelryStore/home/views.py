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
def small_box(request):
    return render(request, 'home/pages/widgets/small-box.html')
def info_box(request):
    return render(request, 'home/pages/widgets/info-box.html')
def general(request):
    return render(request, 'home/pages/UI/general.html')
def icons(request):
    return render(request, 'home/pages/UI/icons.html')
def timeline(request):
    return render(request, 'home/pages/UI/timeline.html')
def simple(request):    
    return render(request, 'home/pages/tables/simple.html')
def theme(request):
    return render(request, 'home/pages/generate/theme.html')
def forms(request):
    return render(request, 'home/pages/forms/general.html')
def main_header(request):
    return render(request, 'home/pages/docs/components/main-header.html')