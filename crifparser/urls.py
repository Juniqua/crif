from django.urls import path,include
from crifparser import views
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView 
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("info_review",views.info_review, name="info_review"),
    path("download_zip",views.download_zip,name="download_zip"),
    path("get_zip", views.get_zip, name='download_zip'),
    path("register", views.registerpage, name="register"),
    path("",views.loginpage, name="login"),
    path("logout",views.logoutuser, name="logout")
]