from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projects_list = [
{
    "id":1,
    "name": "sample prj 1",
    "description": "description 1"
},
{
    "id":2,
    "name": "sample prj 2",
    "description": "description 2"
},
{
    "id":3,
    "name": "sample prj 3",
    "description": "description 3"
}
]

def project(request):
    projects = Project.objects.all()
    number = 10
    return render(request, 'projects/project.html',{'number':number, 'projects':projects})

def projects(request, pk):

    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    return render(request, 'projects/projects.html', {'project':projectobj, 'tags':tags})