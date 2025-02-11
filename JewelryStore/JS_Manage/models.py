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
        return f"{self.maLoaiSP}"

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
    
class hoaDonMuaLai (models.Model):
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
    ngayCapNhat = models.DateTimeField(auto_now=True)
    loaiVang = models.CharField(max_length=100, default='Vàng 9999')
    giaMua = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Thêm giá trị mặc định
    giaBan = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Thêm giá trị mặc định
    donVi = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.loaiVang}  {self.ngayCapNhat}  {self.donVi}"
    
class chuongTrinhKhuyenMai (models.Model):
    maKM = models.CharField(max_length=50, primary_key=True)
    moTa = models.TextField()
    ngayBatDau = models.DateField()
    ngayKetThuc = models.DateField()
    tyLeChietKhau = models.FloatField()
    def __str__(self):
        return f"{self.maKM} {self.moTa} {self.tyLeChietKhau}"

class bangThongKe(models.Model):
    id = models.BigAutoField(primary_key=True)  # Thêm dòng này nếu cần

    ngayCapNhat = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True  # Đánh dấu model này là abstract

class thongKeMuaLaiHang(bangThongKe):
    maSP = models.ForeignKey(sanPham, on_delete=models.CASCADE)
    soLanMua = models.IntegerField()
    tongSoLuong = models.IntegerField()
    tongGiaTri = models.DecimalField(max_digits=18, decimal_places=2)
    
    def __str__(self):
        return f"{self.maSP}  {self.soLanMua}"

class thongKeKhuyenMai(bangThongKe):
    maKM = models.ForeignKey(chuongTrinhKhuyenMai, on_delete=models.CASCADE)
    soLuotSuDung = models.IntegerField()
    tongGiaTriGiam = models.DecimalField(max_digits=18, decimal_places=2)
    ngayBatDau = models.DateField()
    ngayKetThuc = models.DateField()
    
    def __str__(self):
        return f"{self.maKM}  {self.soLuotSuDung}"

class thongKeHieuSuatBanHang(bangThongKe):
    maNV = models.ForeignKey(nhanVien, on_delete=models.CASCADE)
    soDonHang = models.IntegerField()
    tongDoanhThu = models.DecimalField(max_digits=18, decimal_places=2)
    tongSoLuong = models.IntegerField()
    
    def __str__(self):
        return f"{self.maNV}  {self.soDonHang}"

class thongKeDoanhThu(bangThongKe):
    ngay = models.DateField()
    tongDoanhThu = models.DecimalField(max_digits=18, decimal_places=2)
    tongLoiNhuan = models.DecimalField(max_digits=18, decimal_places=2)
    soDonHang = models.IntegerField()
    
    def __str__(self):
        return f"{self.ngay}  Doanh thu: {self.tongDoanhThu}"

class thongKeKhachHang(bangThongKe):
    maKH = models.ForeignKey(khachHang, on_delete=models.CASCADE)
    tongSoDon = models.IntegerField()
    tongGiaTri = models.DecimalField(max_digits=18, decimal_places=2)
    ngayMuaGanNhat = models.DateField()
    
    def __str__(self):
        return f"{self.maKH}  {self.tongSoDon}"

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


