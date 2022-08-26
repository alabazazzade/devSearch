from django.shortcuts import render
from .models import profile
from projects.models import Project

def profiles(request):
    profiles = profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html', context)

def userprofile(request, pk):
    pick_profile = profile.objects.get(id=pk)
    projects = Project.objects.filter(owner=pick_profile)
    context = {
        'profile': pick_profile,
        'projects':projects,
        }
        
    return render(request, 'users/user-profile.html', context)
