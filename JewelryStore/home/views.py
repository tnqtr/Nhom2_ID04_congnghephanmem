from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from JS_Manage.models import nhanVien, bangGiaVang, sanPham, khachHang, hoaDon, hoaDonMuaLai, baoHanh, chuongTrinhKhuyenMai

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
    return render(request, 'home/dashboard/staff.html', {'nhanViens': nhanViens})  # Truyền đúng biến vào template
def bangGiaVang_list(request):
    bangGiaVangs = bangGiaVang.objects.all()
    return render(request, 'home/gold/gold-price.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào template
def sanPham_list(request):
    sanPhams = sanPham.objects.all()
    return render(request, 'home/products/product.html', {'sanPhams': sanPhams})
def khachHang_list(request):
    khachHangs = khachHang.objects.all()
    return render(request, 'home/customers/customer.html', {'khachHangs': khachHangs})
def hoaDon_sold_list(request):
    hoaDons = hoaDon.objects.all()
    return render(request, 'home/bill/bill-sold.html', {'hoaDons': hoaDons})
def hoaDon_back_list(request):
    hoaDonMuaLais = hoaDonMuaLai.objects.all()
    return render(request, 'home/bill/bill-back.html', {'hoaDonMuaLais': hoaDonMuaLais})
def baoHanh_list(request):
    baoHanhs = baoHanh.objects.all()
    return render(request, 'home/warranty/warranty.html', {'baoHanh': baoHanhs})
def chuongTrinhKhuyenMai_list(request):
    chuongTrinhKhuyenMais = chuongTrinhKhuyenMai.objects.all()
    return render(request, 'home/discounts/discount.html', {'chuongTrinhKhuyenMais': chuongTrinhKhuyenMais})
def edit_customer(request, maKH):
    khachHang_obj = get_object_or_404(khachHang, maKH=maKH)
    if request.method == 'POST':
        # Xử lý form và lưu thay đổi
        khachHang_obj.hoTen = request.POST.get('hoTen')
        khachHang_obj.soDT = request.POST.get('soDT')
        khachHang_obj.email = request.POST.get('email')
        khachHang_obj.diemTichLuy = request.POST.get('diemTichLuy')
        khachHang_obj.save()
        return redirect('customers')
    return render(request, 'home/customers/edit-customer.html', {'khachHang': khachHang_obj})
def delete_customer(request, maKH):
    khachHang_obj = get_object_or_404(khachHang, maKH=maKH)
    if request.method == 'POST':
        khachHang_obj.delete()
        return redirect('customers')
    return render(request, 'home/customers/delete-customer.html', {'khachHang': khachHang_obj})
