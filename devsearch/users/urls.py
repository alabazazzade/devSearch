from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('userprofile/<str:pk>/', views.userprofile, name='userprofiles'),
]
