from django.shortcuts import render
from job.models import Job


def dashboard(request):
    return render(request, 'dashboard/home.html')


def job_listing(request):
    jobs = Job.objects.filter(is_available=True)
    context = {'jobs': jobs}
    return render(request, 'dashboard/job_listing.html', context)
