from django.urls import path, include

from login_auth import views

urlpatterns = [
    path('', views.index),
    path('testauth/', views.testauth),
    path('register/', views.register, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
]
