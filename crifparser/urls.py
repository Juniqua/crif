from django.urls import path,include
from crifparser import views
from django.contrib.auth.models import User
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("format_complete",views.format_complete, name="format_complete"),
    #path("", views.index, name='index'),
]