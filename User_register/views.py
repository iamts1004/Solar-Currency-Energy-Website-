from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'User_register/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # creating a form with user input.
        if form.is_valid():  # to check if the same user is not existing already.
            form.save()      # will save the user form data and hash the password in the background.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')  # will create a flask message.
            return redirect('login')   # will redirect it to the login page of the website.
    else:
        form = UserRegisterForm()
    return render(request, 'User_register/register.html', {'form':form})

@login_required  # To make login mandatory to see profile of a user.
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)    # will have current profile info filled in.
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)   # will have current profile picture filled in.
        if u_form.is_valid() and p_form.is_valid():  # to save if the both the form are valid.
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'User_register/profile.html', context)