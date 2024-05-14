from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm

# Register applicant
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            messages.info(request, 'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request, 'Oops!, Something went wrong.')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_applicant.html', context)


# Register recruiter
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            messages.info(request, 'Your account has been created.')
            return redirect('login')
        else:
            messages.warning(request, 'Oops!, Something went wrong.')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)
    

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
            # if request.user.is_applicant:
            #     return redirect('applicant-dashboard')
            # else:
            #     return redirect('recruiter-dashboard')
        else:
            messages.warning(request, 'Oops!, Something went wrong.')
            return redirect('login')
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)
    

def logout_user(request):
    # todo: send message
    logout(request)
    return redirect('login')