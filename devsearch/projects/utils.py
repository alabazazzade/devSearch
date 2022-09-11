from re import search
from django.db.models import Q
from .models import Project, Tag


def searchprojects(request):

    search_prj = ''

    if request.GET.get('search_prj'):
        search_prj = request.GET.get('search_prj')
        tags = Tag.objects.filter(name__icontains=search_prj)

        Projects = Project.objects.distinct().filter(
            Q(title__icontains=search_prj)|
            Q(desctiption__icontains=search_prj)|
            Q(owner__name__icontains=search_prj)|
            Q(tags__in=tags)
            )

        return Projects, search_prj

    projects = Project.objects.all()   
    return projects, search_prj