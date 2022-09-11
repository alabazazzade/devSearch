from django.db.models import Q
from .models import profile, skill


def searchProfiles(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        skills = skill.objects.filter(name__icontains=search_query)

        profiles = profile.objects.distinct().filter(
            Q(name__icontains=search_query)|
            Q(short_intro__icontains=search_query)|
            Q(skill__in=skills)
            )

        return profiles, search_query

    profiles = profile.objects.all()
    return profiles, search_query