from django.urls import path
from . import views


app_name = 'homepage'
urlpatterns = [
    path('', views.home, name = "home"),
    path('logout', views.logout, name = "logout"),
    path('msg', views.msg, name = "msg")
]