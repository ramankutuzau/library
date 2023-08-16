from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', catalog, name='catalog'),
    path('login/', login, name='login'),
    path('create-user/', create_user, name='create_user'),
    path('home/', home, name='home'),
]
