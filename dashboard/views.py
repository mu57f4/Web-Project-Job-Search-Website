from django.shortcuts import render
from job.models import Job


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'dashboard/home.html', context)