from django.contrib import admin
from django.urls import include, path
from .import views
from .views import nhanVien_list

urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("index.html", views.index, name= "index"),
    path("index2.html", views.nhanVien_list, name= "index2"),
    path("index3.html", views.index3, name= "index3"),
    path("forms/general.html", views.forms, name="forms"),
    path("examples/lockscreen.html", views.lockscreen, name="lockscreen"),
    path("examples/login.html", views.login, name="login"),
    path("examples/register.html", views.register, name="register"),
    path("examples/login-v2.html", views.login_v2, name="login-v2"),
    path("examples/register-v2.html", views.register_v2, name="register-v2"),
    path("tables/simple.html", views.simple, name="simple"),
    path("gold/gold-price.html", views.bangGiaVang_list, name="gold-price"),
    path("nhanViens/", views.nhanVien_list, name="nhanVien_list"),
    path("bangGiaVangs/", views.bangGiaVang_list, name="bangGiaVang_list"),
    path("products/product.html", views.sanPham_list, name="products"),
]