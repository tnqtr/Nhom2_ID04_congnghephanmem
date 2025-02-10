from django.contrib import admin
from django.urls import include, path
from .import views
from .views import nhanVien_list


urlpatterns = [
    path("", views.home, name="home"),
    path("home.html", views.home, name="home"),
    path("income.html", views.income, name= "income"),
    path("staff.html", views.nhanVien_list, name= "staff"),
    path("forms/general.html", views.forms, name="forms"),
    path("logout/", views.logout_view, name="logout"),  # Cập nhật URL cho logout
    path("login/", views.login_view, name="login"),
    
    # path("examples/register-v2.html", views.register_v2, name="register-v2"),
    path("tables/simple.html", views.simple, name="simple"),
    path("gold/gold-price.html", views.bangGiaVang_list, name="gold-price"),
    path("nhanViens/", views.nhanVien_list, name="nhanVien_list"),
    path("bangGiaVangs/", views.bangGiaVang_list, name="bangGiaVang_list"),
    path("products/product.html", views.sanPham_list, name="products"),
    path("customers/customer.html", views.khachHang_list, name="customers"),
    path("bill/bill-sold.html", views.hoaDon_sold_list, name="bill-sold"),
    path("bill/bill-back.html", views.hoaDon_back_list, name="bill-back"),
    path("warranty/warranty.html", views.baoHanh_list, name="warranty"),
    path("discounts/discount.html", views.chuongTrinhKhuyenMai_list, name="discounts"),
    path("customers/edit-customer.html/<str:maKH>/", views.edit_customer, name="edit-customer"),
    path("customers/delete-customer/<str:maKH>/", views.delete_customer, name="delete-customer"),
    #path("customers/add-customer.html", views.add_customer, name="add-customer"),
    path("products/edit-product.html/<str:maSP>/", views.edit_product, name="edit-product"),
    path("products/delete-product/<str:maSP>/", views.delete_product, name="delete-product"),
    #path("products/add-product.html", views.add_product, name="add-product"),
    path("discounts/edit-discount.html/<str:maKM>/", views.edit_discount, name="edit-discount"),
    path("discounts/delete-discount/<str:maKM>/", views.delete_discount, name="delete-discount"),
    path("warranty/edit-warranty.html/<str:maBH>/", views.edit_warranty, name="edit-warranty"),
    path("warranty/delete-warranty/<str:maBH>/", views.delete_warranty, name="delete-warranty"),
    path("customers/add-customer.html", views.add_customer, name="add-customer"),
    path("products/add-product.html", views.add_product, name="add-product"),
    path("discounts/add-discount.html", views.add_discount, name="add-discount"),
    path("warranty/add-warranty.html", views.add_warranty, name="add-warranty"),
    path("dashboard/management_dashboard.html", views.management_dashboard, name="management_dashboard"),  # Thêm URL pattern cho management_dashboard
    path("dashboard/staff_dashboard.html", views.staff_dashboard, name="staff_dashboard"),
]   
