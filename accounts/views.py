from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html',
                              {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])

                user.profile.users = request.POST['users']
                user.profile.phonenumber=request.POST['phonenumber']
                user.save()
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'signup.html',
                          {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')