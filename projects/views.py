from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project
from tasks.models import Task
from .serializers import ProjectSerializer
from tasks.serializers import TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing projects and their related tasks.
    """
    queryset = Project.objects.all()
    def get_serializer_class(self):
        """
        Dynamically return the serializer class based on the action.
        """
        if self.action in ['list_tasks']:
            return TaskSerializer  # Use TaskSerializer for task-specific actions
        return ProjectSerializer  # Default to ProjectSerializer for project actions


    @action(detail=True, methods=['get', 'post'], url_path='tasks', url_name='list_tasks')
    def list_tasks(self, request, pk=None):
        """
        Handle both listing tasks (GET) and creating tasks (POST) under the same URL.
        """
        project = self.get_object()  # Get the current project instance
        
        if request.method == 'GET':
            list_tasks = Task.objects.filter(project=project)  # Filter tasks for the project
            serializer = self.get_serializer(list_tasks, many=True)  # Serialize tasks
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)  # Use TaskSerializer for input validation

            if serializer.is_valid():
                serializer.save(project=project)  # Associate the task with the project
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
