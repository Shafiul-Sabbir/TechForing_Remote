from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}} # I am Ensuring the password is write-only field
        
    def create(self, validated_data):
        # Remove the password from validated data and hash it
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user
        