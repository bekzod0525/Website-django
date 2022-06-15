from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

from .forms import SignUpForm


def register(request):
    if request.user.is_authenticated:
        return redirect('userprofile:profile')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user) # biz yaratganuserni login qiladi
            messages.success(request, 'You are now loggen in')
            return redirect('poll:savollar')
    return render(request, 'userprofile/register.html', {'form': SignUpForm()})        


def login_view(request):
    if request.user.is_authenticated:
        return redirect('userprofile:profile')

    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)    
                messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
                return redirect("userprofile:profile")
    return render(request, 'userprofile/login.html', {'form': AuthenticationForm()})

def profile(request):
    return render(request, 'userprofile/profile.html')

def logout_view(request):
    logout(request)
    messages.success(request, ' Tizimdan chiqdingiz!')
    return redirect('home')
