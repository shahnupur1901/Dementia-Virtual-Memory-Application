from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.home, name="home"),
    path('register/',views.registerpage, name="register"),
    path('logout/',views.logoutPage, name="logout"),
    path('login/',views.loginpage, name="login"),
    path('contact/',views.contact, name="contact"),
    path('logout/',views.logout, name="logout"),
]