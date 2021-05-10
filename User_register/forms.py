from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Profile

class UserRegisterForm(UserCreationForm):   # a class for user registration which inherits from UserCreationForm
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.IntegerField()

    class Meta:
        model = User    # will affect the User model
        fields = ['username', 'email', 'address', 'phone', 'password1', 'password2']   # fields we want and their order.

class UserUpdateForm(forms.ModelForm):   # to update the profile info.
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'phone']


class ProfileUpdateForm(forms.ModelForm):   # to update profile picture
    class Meta:
        model = Profile
        fields = ['image']

