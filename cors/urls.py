from django.urls import path 
from rest_framework.routers import DefaultRouter
# from rest_framework import
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# router.register("auth", basename="auth"),
# router.register("profile", basename="profile")


urlpatterns = [
  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls