from django.urls import path,include
from crifparser import views
from django.contrib.auth.models import User
from . import views
urlpatterns = [
    path("home", views.home, name="home"),
    path("info_review",views.info_review, name="info_review"),
    path("download_zip",views.download_zip,name="download_zip"),
    #path("", views.index, name='index'),
]