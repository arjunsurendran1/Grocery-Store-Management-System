#from django.conf.urls import url
from django.urls import include, re_path

from .views import *

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^rice$', display_rice, name="display_rice"),
    re_path(r'^bakery$', display_bakery, name="display_bakery"),
    re_path(r'^dairy$', display_dairy, name="display_dairy"),
    re_path(r'^drinks$', display_drinks, name="display_drinks"),
    re_path(r'^spices$', display_spices, name="display_spices"),

    re_path(r'^add_rice$', add_rice, name="add_rice"),
    re_path(r'^add_bakery$', add_bakery, name="add_bakery"),
    re_path(r'^add_dairy$', add_dairy, name="add_dairy"),
    re_path(r'^add_drinks$', add_drinks, name="add_drinks"),
    re_path(r'^add_spices$', add_spices, name="add_spices"),

    re_path(r'^rice/edit_item/(?P<pk>\d+)$', edit_rice, name="edit_rice"),
    re_path(r'^bakery/edit_item/(?P<pk>\d+)$', edit_bakery, name="edit_bakery"),
    re_path(r'^dairy/edit_item/(?P<pk>\d+)$', edit_dairy, name="edit_dairy"),
    re_path(r'^drinks/edit_item/(?P<pk>\d+)$', edit_drinks, name="edit_drinks"),
    re_path(r'^spices/edit_item/(?P<pk>\d+)$', edit_spices, name="edit_spices"),


    re_path(r'^rice/delete/(?P<pk>\d+)$', delete_rice, name="delete_rice"),
    re_path(r'^bakery/delete/(?P<pk>\d+)$', delete_bakery, name="delete_bakery"),
    re_path(r'^dairy/delete/(?P<pk>\d+)$', delete_dairy, name="delete_dairy"),
    re_path(r'^drinks/delete/(?P<pk>\d+)$', delete_drinks, name="delete_drinks"),
    re_path(r'^spices/delete/(?P<pk>\d+)$', delete_spices, name="delete_spices"),



]
