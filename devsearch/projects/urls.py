from django.urls import path
from projects.views import *

urlpatterns=[
    path('',project,name='projects'),
    path('projects/<str:pk>/',projects,name='projects')
]