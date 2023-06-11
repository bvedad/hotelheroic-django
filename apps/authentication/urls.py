# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from allauth.account import views
from .views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accounts/login/", LoginView.as_view(), name="account_login"),
    path("accounts/logout/", views.logout, name="account_logout"),
    path(
        "accounts/password/change/",
        views.password_change,
        name="account_change_password",
    ),
    path("accounts/password/reset/", views.password_reset, name="account_reset_password"),
    path(
        "accounts/password/reset/done/",
        views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "accounts/password/reset/key/done/",
        views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
    # path('login/', login_view, name="login"),
    # path('register/', register_user, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout")
]
