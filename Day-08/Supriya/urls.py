from django.urls import path
from Supriya import views

urlpatterns = [
    path('',views.home),
    path('demo/',views.chk),
    path('hm/',views.homepage),
    path('lg/',views.lgn),
    path('rg/',views.reg),

 ]

