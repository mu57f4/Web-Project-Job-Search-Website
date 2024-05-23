from django.urls import path
from . import views

app_name = 'job' 

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('manage-jobs/', views.manage_jobs, name='manage-jobs'),
    path('<int:pk>/', views.job_details, name='job_detail'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('all-applicants/<int:pk>/', views.all_applicants, name='all-applicants'),
    path('delete/<int:pk>/', views.delete_job, name='delete-job'),
    path('<int:pk>/num-applicants/', views.get_num_applicants, name='get-num-applicants'),
]