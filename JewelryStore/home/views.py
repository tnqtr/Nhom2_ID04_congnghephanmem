from django.shortcuts import render
from django.http import HttpResponse
from JS_Manage.models import nhanVien, bangGiaVang

# Create your views here.
def home(request):
    return render(request, 'home/home.html ')
def index (request):
    return render(request, 'home/pages/index.html')
def index2 (request):
    return render(request, 'home/pages/index2.html')
def index3 (request):
    return render(request, 'home/pages/index3.html')
def cards(request):
    return render(request, 'home/pages/widgets/cards.html')
def small_box(request):
    return render(request, 'home/pages/widgets/small-box.html')
def info_box(request):
    return render(request, 'home/pages/widgets/info-box.html')
def general(request):
    return render(request, 'home/pages/UI/general.html')
def icons(request):
    return render(request, 'home/pages/UI/icons.html')
def timeline(request):
    return render(request, 'home/pages/UI/timeline.html')
def simple(request):    
    return render(request, 'home/pages/tables/simple.html')
def theme(request):
    return render(request, 'home/pages/generate/theme.html')
def forms(request):
    return render(request, 'home/pages/forms/general.html')
def lockscreen(request):
    return render(request, 'home/pages/examples/lockscreen.html')
def login(request):
    return render(request, 'home/pages/examples/login.html')
def register(request):
    return render(request, 'home/pages/examples/register.html')
def login_v2(request):
    return render(request, 'home/pages/examples/login-v2.html')
def register_v2(request):
    return render(request, 'home/pages/examples/register-v2.html')
def main_header(request):
    return render(request, 'home/pages/docs/components/main-header.html')
def introduction(request):
    return render(request, 'home/pages/docs/introduction.html')
def layout(request):
    return render(request, 'home/pages/docs/layout.html')
def color_mode(request):
    return render(request, 'home/pages/docs/color-mode.html')
def main_sidebar(request):
    return render(request, 'home/pages/docs/components/main-sidebar.html')
def browser_support(request):
    return render(request, 'home/pages/docs/browser-support.html')
def treeview(request):
    return render(request, 'home/pages/docs/javascript/treeview.html')
def how_to_contribute(request):
    return render(request, 'home/pages/docs/how-to-contribute.html')
def faq(request):
    return render(request, 'home/pages/docs/faq.html')
def license(request):
    return render(request, 'home/pages/docs/license.html')
def collapsed_sidebar(request):
    return render(request, 'home/pages/layout/collapsed-sidebar.html')
def fixed_sidebar(request):
    return render(request, 'home/pages/layout/fixed-sidebar.html')
def layout_custom_area(request):
    return render(request, 'home/pages/layout/layout-custom-area.html')
def layout_rtl(request):
    return render(request, 'home/pages/layout/layout-rtl.html')
def logo_switch(request):
    return render(request, 'home/pages/layout/logo-switch.html')
def sidebar_mini(request): 
    return render(request, 'home/pages/layout/sidebar-mini.html')
def unfixed_sidebar(request):
    return render(request, 'home/pages/layout/unfixed-sidebar.html')
def nhanVien_list(request):
    nhanViens = nhanVien.objects.all()  
    return render(request, 'home/pages/index2.html', {'nhanViens': nhanViens})  # Truyền đúng biến vào template
def bangGiaVang_list(request):
    bangGiaVangs = bangGiaVang.objects.all()
    return render(request, 'home/pages/docs/introduction.html', {'bangGiaVangs': bangGiaVangs})  # Truyền đúng biến vào template