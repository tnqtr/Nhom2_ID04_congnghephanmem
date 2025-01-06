from django.urls import path
from . import views

urlpatterns = [
    path('JS_Manage/', views.hoaDon, name='Hoa don'),
    path('JS_Manage/', views.nhanVien, name='Nhan vien'),
]