from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def project(request):
    projects = Project.objects.all()
    number = 10
    return render(request, 'projects/project.html',{'number':number, 'projects':projects})

def projects(request, pk):

    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request, 'projects/projects.html', {'project':projectobj, 'tags':tags})

def createProject(request):
    form =ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

def updateProject(request, pk):
    prj = Project.objects.get(id=pk)
    form =ProjectForm(instance=prj)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES, instance=prj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)

def deleteProject(request, pk):
    prj = Project.objects.get(id=pk)
    # context = {'object':prj}
    if request.method == 'POST':
        prj.delete()
        return redirect('projects')
    return render(request,'projects/delete_object.html')
    # ,context)