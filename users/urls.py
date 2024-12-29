# from django.urls import path
# from .views import RegisterUserView, UserDetailView, LoginUserView
# urlpatterns = [
#     path('register/', RegisterUserView.as_view(), name = 'register_user'),
#     path('<int:pk>/', UserDetailView.as_view(), name = 'user_detail'),
#     path('login/', LoginUserView.as_view(), name = 'login_user'),
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet

# # Create a router and register the CustomUserViewSet
# router = DefaultRouter()
# router.register(r'users', CustomUserViewSet, basename='user')

# # Include the router's URLs in urlpatterns
# urlpatterns = [
#     path('api', include(router.urls)),
# ]
