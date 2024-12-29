from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users with custom actions for register and login.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @action(detail=False, methods=['post'], url_path='register', url_name='register')
    def register(self, request):
        """
        Custom action for user registration.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User registered successfully',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login', url_name='login')
    def login(self, request):
        """
        Custom action for user login.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({
                'error': 'Please provide both username and password.'
            }, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate or retrieve the user's token
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Login successful',
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid username or password.'
            }, status=status.HTTP_401_UNAUTHORIZED)

    



# username : sabbir
# email : shafiulsabbir95@gmail.com
# password : 1234

# Username: jui  
# Email: jui@gmail.com
# password : 1234

# username : yeasin
# email : yeasin@gmail.com
# password : 1234

# username : shishir
# email : shishirkhan@gmail.com
# password : shishir123

# username : tiash
# email : tiash@gmail.com
# password : 1234



