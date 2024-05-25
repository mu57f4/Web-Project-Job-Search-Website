from django.urls import path
from . import views


urlpatterns = [
    path('', views.job_listing, name='dashboard'),
    path('search', views.job_search, name='search'),
]