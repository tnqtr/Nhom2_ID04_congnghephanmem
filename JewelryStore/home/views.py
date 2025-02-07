from django.shortcuts import render
from django.http import HttpResponse
from JS_Manage.models import nhanVien, bangGiaVang, sanPham, khachHang

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def income (request):
    return render(request, 'home/dashboard/income.html')
def staff (request):
    return render(request, 'home/dashboard/staff.html')
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
def simple(request):    
    return render(request, 'home/pages/tables/simple.html')
def nhanVien_list(request):
    nhanViens = nhanVien.objects.all()  
    return render(request, 'home/pages/index2.html', {'nhanViens': nhanViens})  # Truyền đúng biến vào template
def bangGiaVang_list(request):
    bangGiaVangs = bangGiaVang.objects.all()
    return render(request, 'home/gold/gold-price.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào template
def sanPham_list(request):
    sanPhams = sanPham.objects.all()
    return render(request, 'home/products/product.html', {'sanPhams': sanPhams})
def khachHang_list(request):
    khachHangs = khachHang.objects.all()
    return render(request, 'home/customers/customer.html', {'khachHangs': khachHangs})