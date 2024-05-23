from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job 
from applied.models import applied
from .form import CreateJobForm, UpdateJobForm
from django.views.generic import DetailView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

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
                return redirect('job:manage-jobs')
            else:
                messages.warning(request, 'Opps!, something went wrong')
                return redirect('job:create-job')
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
                return redirect('job:manage-jobs')
            else:
                messages.warning(request, 'Opps!, something went wrong')
        else:
            form = UpdateJobForm(instance=job)
            context = {'form': form, 'job': job}
            return render(request, 'job/update_job.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')


def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render(request, 'job/manage_jobs.html', context)


class JobDetailView(DetailView):
    model = Job
    template_name = 'job/job_details.html'
    context_object_name = 'job'


def job_details(request, pk):
    job = get_object_or_404(Job, id=pk)
    already_applied = applied.objects.filter(user=request.user, job=job).exists()
    context = {'job': job, 'already_applied': already_applied}
    return render(request, 'job/job_details.html', context)


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    company = job.company
    if not applied.objects.filter(user=request.user, job=job).exists():
        applied.objects.create(user=request.user, job=job, company=company)
        job.num_applicants += 1
        job.save()
        messages.success(request, 'You application was submited succeccfuly.')
    return redirect('applied:my_applications')\
        
@login_required
def all_applicants(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applicants = applied.objects.filter(job=job)
    context = {'job': job, 'applicants': applicants}
    return render(request, 'job/all_applicants.html', context)


def delete_job(request, pk):
    if request.user.is_authenticated and request.user.is_recruiter and request.user.has_company:
        job = Job.objects.get(pk=pk)
        job.delete()
        messages.success(request, 'Job deleted successfuly.')
        return redirect('job:manage-jobs')
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')
    