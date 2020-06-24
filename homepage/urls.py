from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.home, name = "home"),
    path('logout', views.logout, name = "logout"),
    path('profile', views.profile, name = "profile"),
] 