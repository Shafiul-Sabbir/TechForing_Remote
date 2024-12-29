"""
URL configuration for techforing_pm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('users/', include('users.urls')),
#     path('projects/', include('projects.urls')),
#     path('project-members/', include('project_members.urls')),
#     path('tasks/', include('tasks.urls')),
#     path('comments/', include('comments.urls')),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet
from projects.views import ProjectViewSet
from project_members.views import ProjectMemberViewSet
from tasks.views import TaskViewSet
from comments.views import CommentViewSet

# Create a single router for all resources
router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'project-members', ProjectMemberViewSet, basename='project_member')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

# Include the router's URLs
urlpatterns = [
    path('', include(router.urls)),  # Routes all endpoints defined by the router
]

