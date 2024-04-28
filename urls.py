from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
  path('home', views.homepage) ,
  path('', views.login),
  path('login', views.login),
  path('signup', views.signup),
  path('logout', views.logoutpage)
  # path('services', views.services,name='services'), 
  # path('contact', views.contact,name='contact') ,
  # path('contact/<str:contactid>', views.contactDetails) , #dynamic urls
  # path('about/<aboutid>',views.aboutdetails )
]
