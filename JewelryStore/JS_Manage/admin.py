from django.contrib import admin
from .models import hoaDon, nhanVien, ct_hoadon

# Register your models here.

class hoaDonAd(admin.ModelAdmin):
  list_display = ("id", "ngayTao",)
class nhanVienAd(admin.ModelAdmin):
  list_display = ("hoTen", "maNV",)

admin.site.register(hoaDon,hoaDonAd)
admin.site.register(nhanVien,nhanVienAd)
admin.site.register(ct_hoadon)