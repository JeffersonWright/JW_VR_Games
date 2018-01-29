"""JW_VR_Games URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.urls import re_path

from Games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^Games/(\d+)/', views.game_detail, name='game_detail'),
]
