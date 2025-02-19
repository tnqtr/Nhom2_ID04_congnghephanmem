from django import forms
from JS_Manage.models import khachHang, sanPham, chuongTrinhKhuyenMai, baoHanh, hoaDon


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = khachHang
        fields = ['maKH', 'hoTen', 'soDT', 'email', 'diemTichLuy']

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = sanPham
        fields = ['maSP', 'maLoaiSP', 'tenSP', 'trongLuong', 'tienCong', 'tienDa', 'barcodeSP']

class ChuongTrinhKhuyenMaiForm(forms.ModelForm):
    class Meta:
        model = chuongTrinhKhuyenMai
        fields = ['maKM', 'moTa','ngayBatDau','ngayKetThuc','tyLeChietKhau']

class BaoHanhForm(forms.ModelForm):
    class Meta:
        model = baoHanh
        fields = ['maBH', 'donHangLienKet']

class HoaDonForm(forms.ModelForm):
    class Meta:
        model = hoaDon
        fields = ['maHD', 'ngayTao', 'maKH', 'maNV', 'tongTien']