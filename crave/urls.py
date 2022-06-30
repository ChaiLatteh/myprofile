from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('about', views.about_us, name="about_us"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('careers', views.careers, name="careers"),
]
