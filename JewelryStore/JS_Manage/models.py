from django.db import models

# Create your models here.
class heThong (models.Model):
    maAD = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return self.maAD

class khachHang (models.Model):
    maKH = models.CharField(max_length=10, primary_key=True)
    hoTen = models.CharField(max_length=100)
    soDT = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    diemTichLuy = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.hoTen} {self.maKH}"

class quanLy (models.Model):
    maQL = models.CharField(max_length=10, primary_key=True)
    hoTen = models.CharField(max_length=100)
    quayHangPhuTrach = models.JSONField(default=dict)
    def __str__(self):
        return f"{self.hoTen} {self.maQL}"

class nhanVien (models.Model):
    maNV = models.CharField(max_length=10, primary_key=True)
    hoTen = models.CharField(max_length=100)
    quayHangPhuTrach = models.JSONField(default=dict)
    def __str__(self):
        return f"{self.hoTen} {self.maNV} {self.quayHangPhuTrach}"

class loaiSP (models.Model):
    maLoaiSP = models.CharField(max_length=10, primary_key=True)
    tenLoaiSP = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.tenLoaiSP} {self.maLoaiSP}"

class sanPham (models.Model):
    maSP = models.CharField(max_length=10, primary_key=True)
    maLoaiSP = models.ForeignKey(loaiSP, on_delete=models.CASCADE)
    tenSP = models.CharField(max_length=1000)
    trongLuong = models.DecimalField(max_digits=10, decimal_places=2)
    tienCong = models.DecimalField(max_digits=10, decimal_places=2)
    tienDa = models.DecimalField(max_digits=10, decimal_places=2)
    barcodeSP = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.tenSP} {self.maLoaiSP} {self.maSP}"

class quayHang (models.Model):
    maQH = models.CharField(max_length=10, primary_key=True)
    maQL = models.ForeignKey(quanLy, on_delete=models.CASCADE)
    viTriQH = models.CharField(max_length=1000)
    danhSachNV = models.JSONField(default=dict)
    danhSachSP = models.JSONField(default=dict)
    def __str__(self):
        return self.maQH

class hoaDon (models.Model):
    maHD = models.CharField(max_length=10, primary_key=True, default='DEFAULT_VALUE')
    ngayTao = models.DateField()
    maKH = models.ForeignKey(khachHang, on_delete=models.CASCADE)
    maNV = models.ForeignKey(nhanVien, on_delete=models.CASCADE)
    tongTien = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.maHD} {self.ngayTao}"

class chiTietHD (models.Model):
    maHD = models.ForeignKey(hoaDon, on_delete=models.CASCADE)
    maSP = models.ForeignKey(sanPham, on_delete=models.CASCADE)
    tenSP = models.CharField(max_length=1000)
    soLuong = models.IntegerField()
    giaCa = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.maHD} {self.tenSP} {self.soLuong} {self.giaCa}"

class donHang (models.Model):
    maDH = models.CharField(max_length=10, primary_key=True)
    ngayTao = models.DateField()
    maKH = models.ForeignKey(khachHang, on_delete=models.CASCADE)
    maNV = models.ForeignKey(nhanVien, on_delete=models.CASCADE)
    danhSachSPTrongDH = models.JSONField()
    chietKhauKM = models.FloatField()
    chietKhauDB = models.FloatField()
    def __str__(self):
        return f"{self.maDH} {self.ngayTao} {self.chietKhauKM} {self.chietKhauDB}"

class chiTietDH (models.Model):
    maDH = models.ForeignKey(donHang, on_delete=models.CASCADE)
    maSP = models.ForeignKey(sanPham, on_delete=models.CASCADE)
    tenSP = models.CharField(max_length=1000)
    soLuong = models.IntegerField()
    def __str__(self):
        return f"{self.maDH} {self.tenSP} {self.soLuong}"

class bangGiaVang(models.Model):
    ngayCapNhat = models.DateTimeField()
    loaiVang = models.CharField(max_length=100, default='Vàng 9999')
    giaMua = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Thêm giá trị mặc định
    giaBan = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Thêm giá trị mặc định
    donVi = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.loaiVang} - {self.ngayCapNhat} - {self.donVi}"

class bangThongKe (models.Model):
    doanhThuNV = models.JSONField(default=dict)
    doanhThuQL = models.JSONField(default=dict)
    doanhThuQH = models.JSONField(default=dict)
    tongDoanhThu = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.doanhThuNV} {self.doanhThuQL} {self.doanhThuQH}"

class baoHanh (models.Model):
    maBH = models.CharField(max_length=10, primary_key=True)
    donHangLienKet = models.CharField(max_length=100)
    def __str__(self):
        return self.maBH

class chiTietBH (models.Model):
    maBH = models.ForeignKey(baoHanh, on_delete=models.CASCADE)
    ngayTao = models.DateField()
    ngayKetThuc = models.DateField()
    danhSachLienKet = models.JSONField(default=dict)
    trangThai = models.BooleanField()
    def __str__(self):
        return f"{self.maBH} {self.ngayTao} {self.ngayKetThuc} {self.trangThai}"

class chuongTrinhKhuyenMai (models.Model):
    maKM = models.CharField(max_length=10, primary_key=True)
    moTa = models.TextField()
    ngayBatDau = models.DateField()
    ngayKetThuc = models.DateField()
    tyLeChietKhau = models.FloatField()
    def __str__(self):
        return f"{self.maKM} {self.moTa} {self.tyLeChietKhau}"

