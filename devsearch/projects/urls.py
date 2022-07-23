from django.urls import path
from projects.views import *

urlpatterns=[
    path('project/',project,name='projects'),
    path('projects/',projects,name='projects')
]