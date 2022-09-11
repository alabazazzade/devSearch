from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm, profileform
from .models import profile
from .utils import searchProfiles
from projects.models import Project

def profiles(request):

    profiles, search_query = searchProfiles(request)
    context = {'profiles':profiles, 'search_query':search_query}
    
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    pick_profile = profile.objects.get(id=pk)
    projects = Project.objects.filter(owner=pick_profile)
    context = {
        'profile': pick_profile,
        'projects':projects,
        }
        
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    projects = Project.objects.filter(owner=profile)
    context = {
        'profile':profile,
        'projects':projects,
    }
    return render(request, 'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = profileform(instance=profile)
    context = {
        'form':form,
    }
    if request.method == 'POST':
        form = profileform(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request, 'users/profile_form.html',context)

def loginuser(request):
    page = 'login'
    context = {
        'page':page,
                }
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = user.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request,'username or password is incorrect!')
    return render(request, 'users/login_register.html',context)

def logoutuser(request):
    logout(request)
    messages.success(request,'user was logged out!')
    return redirect('login')


def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {
                'page':page,
                'form':form,
                }
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('profiles')

        else:
            messages.error(request, 'something was wrong in registeration data! ')   

    return render(request, 'users/login_register.html',context)