from django.contrib import admin
from .models import heThong, khachHang, quanLy, nhanVien, loaiSP, sanPham, quayHang, hoaDon, chiTietHD, donHang, chiTietDH, bangGiaVang, bangThongKe, baoHanh, chiTietBH, chuongTrinhKhuyenMai

# Register your models here.
class heThongAd(admin.ModelAdmin):
  list_display = ("maAD",)

class khachHangAd(admin.ModelAdmin):
  list_display = ("hoTen", "maKH",)

class quanLyAd(admin.ModelAdmin):
  list_display = ("hoTen", "maQL",)

class nhanVienAd(admin.ModelAdmin):
  list_display = ("hoTen", "maNV","quayHangPhuTrach",)

class loaiSPAd(admin.ModelAdmin):
  list_display = ("tenLoaiSP", "maLoaiSP",)

class sanPhamAd(admin.ModelAdmin):
  list_display = ("tenSP", "maLoaiSP", "maSP",)

class quayHangAd(admin.ModelAdmin):
  list_display = ("maQH",)

class hoaDonAd(admin.ModelAdmin):
  list_display = ("maHD", "ngayTao",)

class chiTietHDAd(admin.ModelAdmin):
  list_display = ("maHD", "tenSP", "soLuong", "giaCa",)

class donHangAd(admin.ModelAdmin):
  list_display = ("maDH", "ngayTao", "chietKhauKM", "chietKhauDB",)

class chiTietDHAd(admin.ModelAdmin):
  list_display = ("maDH", "tenSP", "soLuong",)

class bangGiaVangAd(admin.ModelAdmin):
  list_display = ("ngayCapNhat",)

class bangThongKeAd(admin.ModelAdmin):
  list_display = ("doanhThuNV", "doanhThuQL", "doanhThuQH",)

class baoHanhAd(admin.ModelAdmin):
  list_display = ("maBH",)

class chiTietBHAd(admin.ModelAdmin):
  list_display = ("maBH", "ngayTao", "ngayKetThuc", "trangThai",)

class chuongTrinhKhuyenMaiAd(admin.ModelAdmin):
  list_display = ("maKM", "moTa", "tyLeChietKhau",)

admin.site.register(heThong,heThongAd)

admin.site.register(khachHang,khachHangAd)

admin.site.register(quanLy,quanLyAd)

admin.site.register(nhanVien,nhanVienAd)

admin.site.register(loaiSP,loaiSPAd)

admin.site.register(sanPham,sanPhamAd)

admin.site.register(quayHang,quayHangAd)

admin.site.register(hoaDon,hoaDonAd)

admin.site.register(chiTietHD,chiTietHDAd)

admin.site.register(donHang,donHangAd)

admin.site.register(chiTietDH,chiTietDHAd)

admin.site.register(bangGiaVang,bangGiaVangAd)

admin.site.register(bangThongKe,bangThongKeAd)

admin.site.register(baoHanh,baoHanhAd)

admin.site.register(chiTietBH,chiTietBHAd)

admin.site.register(chuongTrinhKhuyenMai,chuongTrinhKhuyenMaiAd)
