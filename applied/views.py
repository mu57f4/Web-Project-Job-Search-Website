from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import applied
from job.models import Job
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

@login_required
def ajax_applied_list(request):
    applied_jobs = applied.objects.filter(user=request.user)
    data = []
    for applied_job in applied_jobs:
        job = applied_job.job
        data.append({
            'title': job.title,
            'location': job.location,
            'salary': f"{job.salary:,}" if job.salary else "NA",
            'job_type': job.job_type,
            'applied_date': applied_job.applied_date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse(data, safe=False)