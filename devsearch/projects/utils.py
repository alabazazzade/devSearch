from re import search
from django.db.models import Q
from .models import Project, Tag

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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

def projectpagination(request, projects, results):
    page = request.GET.get('page')
    results = results
    try:
        paginator = Paginator(projects, results)
        print(page)
        Right_limit = int(page) - 5
        if Right_limit < 1:
            Right_limit = 1
    
        Left_limit = int(page) + 5
        if Left_limit > paginator.num_pages:
            Left_limit = paginator.num_pages
        
        custom_range = range(Right_limit,Left_limit)
        # return page, paginator, custom_range
        
    except:
        page = 1
        paginator = Paginator(projects, results)
     
    # except EmptyPage:
    #     page = paginator.num_pages
    #     paginator = Paginator(projects, results)
        
    print(page)
    Right_limit = int(page) - 1
    if Right_limit < 1:
        Right_limit = 1
    
    Left_limit = int(page) + 1
    if Left_limit > paginator.num_pages:
        Left_limit = paginator.num_pages
        
    custom_range = range(Right_limit,Left_limit)
    return page, paginator, custom_range