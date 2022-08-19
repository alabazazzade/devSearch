from django.urls import path
from projects.views import *

urlpatterns=[
    path('',project,name='projects'),
    path('projects/<str:pk>/',projects,name='projects'),
    path('create-project/',createProject, name="create-project"),
    path('update-project/<str:pk>/',updateProject, name='update-project'),
    path('delete-project/<str:pk>/',deleteProject, name='delete-project'),
]