from django import forms
from JS_Manage.models import khachHang

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = khachHang
        fields = ['maKH', 'hoTen', 'soDT', 'email', 'diemTichLuy']