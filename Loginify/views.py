from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!!!")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')
        
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Signup successful! Please log in.')
        return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f'Welcome, {user.username}!')
            return render(request, 'login_success.html', {'user': user})  # Pass user object to template

        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'login.html')