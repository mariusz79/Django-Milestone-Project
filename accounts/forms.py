from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    email = forms.EmailField(required=True)
    username = forms.CharField(label="Username", min_length=5, max_length=30)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            self._errors['username'] = self.error_class(
                ['Minimum 5 characters required'])
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")

        if password1 != password2:
            raise ValidationError("Passwords must match")

        return password2

class UserUpdateForm(forms.ModelForm):
    """Form used to update user's email"""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    """Form used to update user's profile image"""
    class Meta:
        model = Profile
        fields = ['image']