#!/usr/bin/env python3

from django.urls import path
from . import views


app_name = 'backend'  # here for namespacing of urls.

urlpatterns = [
    path('',views.login,name='login'),
    path('battle/', views.battle, name='battle'),
    path('battle/win.html', views.win, name='win'),
    path('battle/lose.html', views.lose, name='lose')
]
