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
    path('thong-ke-mua-lai/', views.thong_ke_mua_lai, name='Thong ke mua lai'),
    path('thong-ke-khuyen-mai/', views.thong_ke_khuyen_mai, name='Thong ke khuyen mai'),
    path('thong-ke-hieu-suat/', views.thong_ke_hieu_suat, name= 'Thong ke hieu suat'),
    path('thong-ke-doanh-thu/', views.thong_ke_doanh_thu, name='Thong ke doanh thu'),
    path('thong-ke-khach-hang/', views.thong_ke_khach_hang, name='Thong ke khach hang'),
    path('bao-hanh/', views.bao_hanh_view, name='Bao hanh'),
    path('chi-tiet-bao-hanh/', views.chi_tiet_bao_hanh_view, name='Chi tiet bao hanh'),
    path('chuong-trinh-khuyen-mai/', views.chuong_trinh_khuyen_mai_view, name='Chuong trinh khuyen mai'),
]
