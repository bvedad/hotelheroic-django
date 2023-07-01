# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import render


@login_required
def index_view(request):
    return redirect('dashboard')

@login_required
def dashboard_view(request):
    return render(request, 'home/dashboard.html')


@login_required
def calendar_view(request):
    return render(request, 'home/calendar.html')


@login_required
def reservations_view(request):
    return render(request, 'home/reservations.html')


@login_required
def groups_view(request):
    return render(request, 'home/groups.html')


@login_required
def house_account_view(request):
    return render(request, 'home/house-account.html')


@login_required
def guests_view(request):
    return render(request, 'home/guests.html')


@login_required
def reports_view(request):
    return render(request, 'home/reports.html')
