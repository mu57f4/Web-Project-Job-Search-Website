from django.shortcuts import render


def dashboard(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    return render(
        request, 'dashboard/dashboard.html',
        {'username': username}
        )
