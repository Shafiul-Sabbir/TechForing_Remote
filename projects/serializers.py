from rest_framework import serializers
from .models import Project
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),
    write_only=True)
    
    owner_details = serializers.SerializerMethodField()
    
    class Meta: 
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'owner_details']  
        
    def get_owner_details(self, obj):
        """Custom field to include limited owner details."""
        return {
            "id": obj.owner.id,
            "username": obj.owner.username,
            "email": obj.owner.email
        }

   