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
]