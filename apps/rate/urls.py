from django.urls import path

from apps.rate import views

urlpatterns = [
    path('', views.rates_availability_view, name='rates_availability'),
    path('rates/', views.RateIntervalListView.as_view(), name='rate_interval_index'),
    path('rates/<int:pk>/edit/', views.rate_interval_edit_view, name='rate_interval_edit'),
    path('rates/create/', views.rate_interval_create_view, name='rate_interval_create'),
]
