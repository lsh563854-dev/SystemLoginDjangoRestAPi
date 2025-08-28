from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenVerifyView,
TokenRefreshView
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name="token"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('api/login/', views.login, name="login"),
    path('api/register/', views.register, name="register"),
    path('api/logout/', views.logout, name="logout"),
]
