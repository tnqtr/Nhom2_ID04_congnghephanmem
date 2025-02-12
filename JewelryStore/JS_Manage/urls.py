from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='Admin'),
    path('khach-hang/', views.khach_hang_view, name='Khach hang'),
    path('quan-ly/', views.quan_ly_view, name='Quan ly'),
    path('nhan-vien/', views.nhan_vien_view, name='Nhan vien'),
    path('loai-san-pham/', views.loai_san_pham_view, name='Loai san pham'),
    path('san-pham/', views.san_pham_view, name='San pham'),
    path('quay-hang/', views.quay_hang_view, name='Quay hang'),
    path('hoa-don/', views.hoa_don_view, name='Hoa don'),
    path('chi-tiet-hoa-don/', views.chi_tiet_hoa_don_view, name='Chi tiet hoa don'),
    path('don-hang/', views.don_hang_view, name='Don hang'),
    path('chi-tiet-don-hang/', views.chi_tiet_don_hang_view, name='Chi tiet don hang'),
    path('bang-gia-vang/', views.bang_gia_vang_view, name='Bang gia vang'),
    path('bang-thong-ke/', views.bang_thong_ke_view, name='Bang thong ke'),
    path('bao-hanh/', views.bao_hanh_view, name='Bao hanh'),
    path('chi-tiet-bao-hanh/', views.chi_tiet_bao_hanh_view, name='Chi tiet bao hanh'),
    path('chuong-trinh-khuyen-mai/', views.chuong_trinh_khuyen_mai_view, name='Chuong trinh khuyen mai'),
]
