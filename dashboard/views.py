from django.shortcuts import render
from job.models import Job
from .filter import JobFilter


def job_listing(request):
    jobs = Job.objects.filter(is_available=True).order_by('-timestamp')
    context = {'jobs': jobs}
    return render(request, 'dashboard/home.html', context)


def job_search(request):
    filter = JobFilter(
        request.GET,
        queryset=Job.objects.filter(is_available=True).order_by('-timestamp')
        )
    context = {'filter': filter}
    return render(request, 'dashboard/search.html', context)