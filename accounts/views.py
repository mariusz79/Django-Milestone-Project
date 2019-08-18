from django.shortcuts import render
from django.shortcuts import render, redirect, reverse 
from django.contrib import auth, messages
from django.contrib.auth.models import User 
from .forms import UserRegistrationForm

# Create your views here.
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request,
                               "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm(None)
    return render(request, 'registration.html',
                  {"registration_form": registration_form})