from django.db import models

# Create your models here.
class hoaDon (models.Model):
    ngayTao = models.DateField()
    maKH = models.CharField(max_length=10)
    maNV = models.CharField(max_length=10)
    tongTien = models.IntegerField()
    def __str__(self):
        return f"{self.id} {self.ngayTao}"

class nhanVien (models.Model):
    maNV = models.CharField(max_length=10)
    hoTen = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.hoTen} {self.maNV}"