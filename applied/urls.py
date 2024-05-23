from django.urls import path
from .import views

app_name = 'applied'

urlpatterns = [
    path('', views.AppliedListView.as_view(), name='applied_list'),
    path('my-applications/', views.applied_list, name='my_applications'),
]