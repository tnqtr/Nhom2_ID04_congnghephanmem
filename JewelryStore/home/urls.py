from django.contrib import admin
from django.urls import include, path
from .import views

urlpatterns = [
    
    path("", views.home, name= "home"),
    path("index.html", views.index, name= "index"),
    path("index2.html", views.index2, name= "index2"),
    path("index3.html", views.index3, name= "index3"),
    path("widgets/cards.html", views.cards, name="cards"),
    path("admin/", admin.site.urls),
    
]