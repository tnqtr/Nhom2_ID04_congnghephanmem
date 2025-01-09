from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('JS_Manage/', views.hoaDon, name='Hoa don'),
    path('JS_Manage/', views.nhanVien, name='Nhan vien'),
]