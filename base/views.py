from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import User, ChatMessage, CodeMessage, CourseInformation
from .forms import (
    MyUserCreationFrom, ChatAIForm,
    ChatUserForm, CodeUserForm, CodeAIForm,
    CourseForm, UserForm
)

def home(request):
    response = ''
    context = {}
    return render(request, 'base/home.html', context)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username OR password does not match")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('home')

def UpdateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method =="POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home') #home will have a pk
        else:
            messages.error(request, form.errors)

    return render(request, 'base/update_user.html', {"form": form})


def registerUser(request):
    form = MyUserCreationFrom()
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = MyUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, form.errors)

    return render(request, 'base/login_register.html', {'form': form})


def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            #return redirect('update-user')
        else:
            messages.error(request, form.errors)
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'base/change_password.html', {"form": form})

def settings(request):
    #other code to be written here
    return render(request, 'base/settings.html')

def deleteUser(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    else:
        messages.error(request, 'An error occured deleting your account')
        return redirect('settings')


def userProfile(request):
    user = User.objects.get(id=request.user.id)
    context = {"user": user}
    return render(request, 'base/profile.html', context)





