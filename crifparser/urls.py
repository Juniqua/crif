from django.urls import path,include
from crifparser import views
from django.contrib.auth.models import User
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("info_review",views.info_review, name="info_review"),
    #path("", views.index, name='index'),
]