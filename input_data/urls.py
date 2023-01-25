from django.urls import path, include

from input_data import views

urlpatterns = [
    path('', views.index),
    path('start', views.test),
    path('index', views.index),
    path('st2', views.st2),
    path('form_in', views.form_in),
    path('form_tabs', views.form_tabs),
    path('form_list', views.form_list),
]