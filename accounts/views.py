from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('home'))
            else:
                messages.error(request,
                               "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm(None)
    return render(request, 'registration.html',
                  {"registration_form": registration_form})

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('home'))

@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    group = Group.objects.get(name="paid").user_set.all()

    bugs = Bug.objects.filter(
        author=user).order_by('-published_date')

    features = Feature.objects.filter(
        author=user).order_by('-published_date')


    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'group': group,
        'bugs': bugs,
        'features': features
    }



    return render(request, 'profile.html', context)



def other_user_profile(request, username):
    """ The others user's profile page """

    # get user object using username
    user = get_object_or_404(User, username=username)
    group = Group.objects.get(name="paid").user_set.all()

    bugs = Bug.objects.filter(author=user).order_by('-published_date')

    features = Feature.objects.filter(author=user).order_by('-published_date')

    context = {
        'group': group,
        'bugs': bugs,
        'features': features,
        'user': user
    }

    return render(request, "otheruserprofile.html", context)