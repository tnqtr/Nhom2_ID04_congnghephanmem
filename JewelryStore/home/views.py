from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from JS_Manage.models import nhanVien, bangGiaVang, sanPham, khachHang, hoaDon, hoaDonMuaLai, baoHanh, chuongTrinhKhuyenMai, loaiSP
from .forms import KhachHangForm, SanPhamForm, ChuongTrinhKhuyenMaiForm, BaoHanhForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def home(request):
    return render(request, 'home/home.html')
def income (request):
    return render(request, 'home/dashboard/income.html')
def staff (request):
    return render(request, 'home/dashboard/staff.html')
def forms(request):
    return render(request, 'home/pages/forms/general.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')  # Chuyển hướng đến trang admin của Django
                elif user.is_staff:
                    return redirect('management_dashboard')  # Chuyển hướng đến trang quản lý
                else:
                    return redirect('staff_dashboard')  # Chuyển hướng đến trang nhân viên
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'home/pages/login/login.html', {'form': form})

@login_required
def management_dashboard(request):
    return render(request, 'home/dashboard/management_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'home/dashboard/staff_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# def login(request):
#     return render(request, 'home/pages/login/login.html')
# def register(request):
#     return render(request, 'home/pages/examples/register.html')
# def login(request):
#     return render(request, 'home/pages/login/login.html')
# def register(request):
#     return render(request, 'home/pages/login/register.html')
def simple(request):    
    return render(request, 'home/pages/tables/simple.html')

# Staff App
def nhanVien_list(request):
    nhanViens = nhanVien.objects.all()  
    return render(request, 'home/dashboard/staff.html', {'nhanViens': nhanViens})  # Truyền đúng biến vào template

# Gold App
def bangGiaVang_list(request):
    bangGiaVangs = bangGiaVang.objects.all()
    return render(request, 'home/gold/gold-price.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào template

# Bill App
def hoaDon_sold_list(request):
    hoaDons = hoaDon.objects.all()
    return render(request, 'home/bill/bill-sold.html', {'hoaDons': hoaDons})

def hoaDon_back_list(request):
    hoaDonMuaLais = hoaDonMuaLai.objects.all()
    return render(request, 'home/bill/bill-back.html', {'hoaDonMuaLais': hoaDonMuaLais})

# Warranty App
def baoHanh_list(request):
    baoHanhs = baoHanh.objects.all()
    return render(request, 'home/warranty/warranty.html', {'baoHanhs': baoHanhs})

def edit_warranty(request, maBH):
    baoHanh_obj = get_object_or_404(baoHanh, maBH=maBH)
    if request.method == 'POST':
        baoHanh_obj.maBH = request.POST.get('maBH')
        baoHanh_obj.ngayCapNhat = request.POST.get('ngayCapNhat')
        baoHanh_obj.maKH = request.POST.get('maKH')
        baoHanh_obj.maNV = request.POST.get('maNV')
        baoHanh_obj.save()
        return redirect('warranty')
    return render(request, 'home/warranty/edit-warranty.html', {'baoHanh': baoHanh_obj})

def delete_warranty(request, maBH):
    baoHanh_obj = get_object_or_404(baoHanh, maBH=maBH)
    if request.method == 'POST':
        baoHanh_obj.delete()
        return redirect('warranty')
    return render(request, 'home/warranty/delete-warranty.html', {'baoHanh': baoHanh_obj})

def add_warranty(request):
    if request.method == 'POST':
        form = BaoHanhForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warranty')
    else:
        form = BaoHanhForm()
    return render(request, 'home/warranty/add-warranty.html', {'form': form})

# Discount App
def chuongTrinhKhuyenMai_list(request):
    chuongTrinhKhuyenMais = chuongTrinhKhuyenMai.objects.all()
    return render(request, 'home/discounts/discount.html', {'chuongTrinhKhuyenMais': chuongTrinhKhuyenMais})

def add_discount(request):
    if request.method == 'POST':
        form = ChuongTrinhKhuyenMaiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discounts')
    else:
        form = ChuongTrinhKhuyenMaiForm()
    return render(request, 'home/discounts/add-discount.html', {'form': form})

# Customer App
def khachHang_list(request):
    khachHangs = khachHang.objects.all()
    return render(request, 'home/customers/customer.html', {'khachHangs': khachHangs})

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

def add_customer(request):
    if request.method == 'POST':
        form = KhachHangForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = KhachHangForm()
    return render(request, 'home/customers/add-customer.html', {'form': form})

# Product App
def sanPham_list(request):
    sanPhams = sanPham.objects.all()
    return render(request, 'home/products/product.html', {'sanPhams': sanPhams})

def edit_product(request, maSP):
    sanPham_obj = get_object_or_404(sanPham, maSP=maSP)
    if request.method == 'POST':
        maLoaiSP = request.POST.get('maLoaiSP')
        loaiSP_obj = get_object_or_404(loaiSP, maLoaiSP=maLoaiSP)
        sanPham_obj.maLoaiSP = loaiSP_obj
        sanPham_obj.tenSP = request.POST.get('tenSP')
        sanPham_obj.trongLuong = request.POST.get('trongLuong')
        sanPham_obj.tienCong = request.POST.get('tienCong')
        sanPham_obj.tienDa = request.POST.get('tienDa')
        sanPham_obj.barcodeSP = request.POST.get('barcodeSP')
        sanPham_obj.save()
        return redirect('products')
    return render(request, 'home/products/edit-product.html', {'sanPham': sanPham_obj})

def delete_product(request, maSP):
    sanPham_obj = get_object_or_404(sanPham, maSP=maSP)
    if request.method == 'POST':
        sanPham_obj.delete()
        return redirect('products')
    return render(request, 'home/products/delete-product.html', {'sanPham': sanPham_obj})

def edit_discount(request, maKM):
    chuongTrinhKhuyenMai_obj = get_object_or_404(chuongTrinhKhuyenMai, maKM=maKM)
    if request.method == 'POST':
        chuongTrinhKhuyenMai_obj.moTa = request.POST.get('moTa')
        chuongTrinhKhuyenMai_obj.tyLeChietKhau = request.POST.get('tyLeChietKhau')
        chuongTrinhKhuyenMai_obj.save()
        return redirect('discounts')
    return render(request, 'home/discounts/edit-discount.html', {'chuongTrinhKhuyenMai': chuongTrinhKhuyenMai_obj})
def delete_discount(request, maKM):
    chuongTrinhKhuyenMai_obj = get_object_or_404(chuongTrinhKhuyenMai, maKM=maKM)
    if request.method == 'POST':
        chuongTrinhKhuyenMai_obj.delete()
        return redirect('discounts')
    return render(request, 'home/discounts/delete-discount.html', {'chuongTrinhKhuyenMai': chuongTrinhKhuyenMai_obj})

def add_product(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = SanPhamForm()
    return render(request, 'home/products/add-product.html', {'form': form})

# Sell App
def sell(request):
    sanPhams = sanPham.objects.all()
    return render(request, 'home/sell/sell.html', {'sanPhams': sanPhams})
    