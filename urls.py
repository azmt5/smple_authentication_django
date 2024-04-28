from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
  path('home', views.homepage) ,
  path('', views.login),
  path('login', views.login),
  path('signup', views.signup),
  path('logout', views.logoutpage)

]
