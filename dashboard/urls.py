from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_listing, name='dashboard'),
]