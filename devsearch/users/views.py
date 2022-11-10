from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm, profileform, SkillForm
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

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)
