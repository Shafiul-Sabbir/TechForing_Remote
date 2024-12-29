from rest_framework import viewsets
from .models import Task
from comments.models import Comment
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from comments.serializers import CommentSerializer  

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing tasks.
    """
    queryset = Task.objects.all()
    def get_serializer_class(self):
        """
        Dynamically return the serializer class based on the action.
        """
        if self.action in ['list_comments', 'create_comment']:
            return CommentSerializer  # Use CommentSerializer for comment-specific actions
        return TaskSerializer  # Default to TaskSerializer for task actions

    @action(detail=True, methods=['get', 'post'], url_path='comments', url_name='list_comments')
    def list_comments(self, request, pk=None):
        """
        Handle both listing comments (GET) and creating comments (POST) under the same URL.
        """
        task = self.get_object()  # Get the current task instance
        
        if request.method == 'GET':
            list_comments = Comment.objects.filter(task=task)  # Filter comments for the task
            serializer = self.get_serializer(list_comments, many=True)  # Serialize comments
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = self.get_serializer(data=request.data)  # Use CommentSerializer for input validation

            if serializer.is_valid():
                serializer.save(task=task)  # Associate the task with the project   
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

