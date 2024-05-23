from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import applied
from job.models import Job

class AppliedListView(ListView):
    model = applied
    template_name = 'applied/applied_list.html'
    context_object_name = 'applied_jobs'

    def get_queryset(self):
        return applied.objects.filter(user=self.request.user).select_related('job', 'company')

def applied_list(request):
    applied_jobs = applied.objects.filter(user=request.user)
    job_ids = applied_jobs.values_list('job_id', flat=True)
    jobs = Job.objects.filter(id__in=job_ids)
    context = {'applied_jobs':applied_jobs, 'jobs': jobs}
    return render(request, 'applied/applied_list.html', context)