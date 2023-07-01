# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    path('', views.index_view, name='index'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('reservations/', views.reservations_view, name='reservations'),
    path('groups/', views.groups_view, name='groups'),
    path('house-account/', views.house_account_view, name='house_account'),
    path('guests/', views.guests_view, name='guests'),
    path('reports/', views.reports_view, name='reports'),
]
