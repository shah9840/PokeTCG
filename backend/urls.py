#!/usr/bin/env python3

from django.urls import path
from . import views


app_name = 'backend'  # here for namespacing of urls.

urlpatterns = [
    path('',views.login,name="login"),
    path('battle', views.homepage, name="homepage"),
]
