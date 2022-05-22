from django.urls import path,include
from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.posts, name='posts')
    
]