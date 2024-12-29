from rest_framework import viewsets
from .models import ProjectMember
from .serializers import ProjectMemberSerializer

class ProjectMemberViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing project members.
    """
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
