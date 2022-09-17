from email.message import Message
from urllib.error import HTTPError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import AnonymousUser

from .models import Project, Review
from .forms import ProjectForm,ReviewForm
from .utils import searchprojects, projectpagination



def project(request):

    projects, search_prj = searchprojects(request)
    page, paginator, custom_range = projectpagination(request, projects, 6)
    projects = paginator.page(page)
    return render(request, 'projects/project.html',
                {'projects':projects, 'search_prj':search_prj,
                 'paginator':paginator, 'custom_range':custom_range})
    
def projects(request, pk):
    try:
        projectobj = Project.objects.get(id=pk)
        tags = projectobj.tags.all()
        reviews = projectobj.review_set.all()
        form = ReviewForm()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            review = form.save(commit=False)
            review.project = projectobj
            review.owner = request.user.profile
            review.save()
            projectobj.getVoteCount # this is written in the models and keeps vote total and vote ratio updated
            messages.success(request,message='Your Review was updated successfully')
            
        return render(request, 'projects/projects.html', {'project':projectobj, 'tags':tags,
                                                      'reviews':reviews, 'form':form})
    except IntegrityError:
        messages.error(request, message='You have already commented on this project')
        return redirect('projects', pk=projectobj.id)
    
    except Exception as e:
        messages.error(request, message='You have to login in order to leave a comment on a project')
        return redirect('login')

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form =ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            new_prj = form.save(commit=False)
            new_prj.owner = profile
            new_prj.save()

            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    prj = profile.project_set.get(id=pk)
    form =ProjectForm(instance=prj)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=prj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    prj = profile.project_set.get(id=pk)
    # context = {'object':prj}
    if request.method == 'POST':
        prj.delete()
        return redirect('projects')
    return render(request,'projects/delete_object.html')
    # ,context)