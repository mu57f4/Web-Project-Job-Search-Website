from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('job-listing/', views.job_listing, name='job-listing'),
]