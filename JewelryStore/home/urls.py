from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    
    path("", views.home, name= "home"),
    path("index.html", views.index, name= "index"),
    path("index2.html", views.index2, name= "index2"),
    path("index3.html", views.index3, name= "index3"),
    path("widgets/cards.html", views.cards, name="cards"),
    path("widgets/small-box.html", views.small_box, name="small-box"),
    path("widgets/info-box.html", views.info_box, name="info-box"),
    path("UI/general.html", views.general, name="general"),
    path("UI/icons.html", views.icons, name="icons"),
    path("UI/timeline.html", views.timeline, name="timeline"),
    path("tables/simple.html", views.simple, name="simple"),
    path("generate/theme.html", views.theme, name="theme"),
    path("forms/general.html", views.forms, name="forms"),
    path("examples/lockscreen.html", views.lockscreen, name="lockscreen"),
    path("examples/login.html", views.login, name="login"),
    path("examples/register.html", views.register, name="register"),
    path("examples/login-v2.html", views.login_v2, name="login-v2"),
    path("examples/register-v2.html", views.register_v2, name="register-v2"),
    path("docs/components/main-header.html", views.main_header, name="main-header"),
    path("docs/introduction.html", views.introduction, name="introduction"),
    path("docs/layout.html", views.layout, name="layout"),
    path("docs/color-mode.html", views.color_mode, name="color-mode"),
    path("docs/components/main-sidebar.html", views.main_sidebar, name="main-sidebar"),
    path("docs/browser-support.html", views.browser_support, name="browser-support"),
    path("docs/javascript/treeview.html", views.treeview, name="treeview"),
    path("docs/how-to-contribute.html", views.how_to_contribute, name="how-to-contribute"),
    path("docs/faq.html", views.faq, name="faq"),
    path("docs/license.html", views.license, name="license"),
    path("layout/collapsed-sidebar.html", views.collapsed_sidebar, name="collapsed-sidebar"),
    path("layout/fixed-sidebar.html", views.fixed_sidebar, name="fixed-sidebar"),
    path("layout/layout-custom-area.html", views.layout_custom_area, name="layout-custom-area"),
    path("layout/layout-rtl.html", views.layout_rtl, name="layout-rtl"),
    path("layout/logo-switch.html", views.logo_switch, name="logo-switch"),
    path("layout/sidebar-mini.html", views.sidebar_mini, name="sidebar-mini"),
    path("layout/unfixed-sidebar.html", views.unfixed_sidebar, name="unfixed-sidebar"),
    
]