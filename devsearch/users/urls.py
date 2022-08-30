from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('userprofile/<str:pk>/', views.userprofile, name='userprofiles'),

    path('login/',views.loginuser,name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registeruser, name='register'),
    path('account/', views.userAccount, name='account'),
    path('editaccount/', views.editAccount, name='edit-account'),
]
