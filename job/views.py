from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .form import CreateJobForm, UpdateJobForm


def create_job(request):
    if request.user.is_authenticated and request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.success(request, 'New job has been created.')
                return redirect('manage-jobs')
            else:
                messages.warning(request, 'Opps!, something went wrong')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create_job.html', context=context)
    else:
        # todo: send message if is_recruiter
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


def update_job(request, pk):
    if request.user.is_authenticated and request.user.is_recruiter and request.user.has_company:
        job = Job.objects.get(pk=pk)
        if request.method == 'POST':
            form = UpdateJobForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                messages.success(request, 'Job info has been updated successfully.')
                return redirect('manage-jobs')
            else:
                messages.warning(request, 'Opps!, something went wrong')
        else:
            form = UpdateJobForm(instance=job)
            context = {'form': form}
            return render(request, 'job/update_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render(request, 'job/manage_jobs.html', context)


def job_details(request, pk):
    job = Job.objects.get(pk=pk)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)