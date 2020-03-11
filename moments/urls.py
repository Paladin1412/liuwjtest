# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.home),
    url(r'^user/$', views.show_user),
    url(r'^status/$', views.show_status),
    url(r'^post/$', views.show_post),
    # url(r'^$', views.home),
    # url(r'^dev-guide/$', views.dev_guide),
    # url(r'^contact/$', views.contact),
)
