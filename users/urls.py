
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from .views import profile


# url patterns under ('u/')
urlpatterns = [

    # user/profile urls
    path('<str:username>/', profile, name='profile'),

]