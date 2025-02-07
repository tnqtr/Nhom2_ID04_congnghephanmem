from django.shortcuts import render
from django.http import HttpResponse
from JS_Manage.models import nhanVien, bangGiaVang, sanPham

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def index (request):
    return render(request, 'home/pages/index.html')
def index2 (request):
    return render(request, 'home/pages/index2.html')
def index3 (request):
    return render(request, 'home/pages/index3.html')
def forms(request):
    return render(request, 'home/pages/forms/general.html')
def lockscreen(request):
    return render(request, 'home/pages/examples/lockscreen.html')
def login(request):
    return render(request, 'home/pages/examples/login.html')
def register(request):
    return render(request, 'home/pages/examples/register.html')
def login_v2(request):
    return render(request, 'home/pages/examples/login-v2.html')
def register_v2(request):
    return render(request, 'home/pages/examples/register-v2.html')
def nhanVien_list(request):
    nhanViens = nhanVien.objects.all()  
    return render(request, 'home/pages/index2.html', {'nhanViens': nhanViens})  # Truyền đúng biến vào template
def bangGiaVang_list(request):
    bangGiaVangs = bangGiaVang.objects.all()
<<<<<<< HEAD
    return render(request, 'home/pages/docs/introduction.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào templ
def sanPham_list(request):
    sanPhams = sanPham.objects.all()
    return render(request, 'home/products/product.html', {'sanPhams': sanPhams})
=======
    return render(request, 'home/pages/gold/gold-price.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào template
>>>>>>> 21e4d4f40c5a865515c7602e1ac9f4ccdd31734e
