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
    path('form_users', views.form_users),
    path('delete_user', views.form_delete_user),
    path('equipments', views.form_equipments),
    path('equip_add', views.form_add_equipment),
    path('get_all_data', views.get_all_equipments),
    path('add_unit', views.form_units),
    path('add_position', views.form_position),
    path('conf_comp', views.config_computer_manual),
    path('conf_auto', views.config_computer_auto),
    path('conf_as_file', views.config_computer_file),
]