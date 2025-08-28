from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password:
        return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username, email=email, password=password)
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "login successful",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
            "id": user.id
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def logout(request):
    try:
        tokenss = request.data["refresh"]
        tokenm = RefreshToken(tokenss)
        tokenm.blacklist()
        return Response({"message":"logout successful"},status=status.HTTP_200_OK)
    except:
        return Response({"message":"logout failed"},status=status.HTTP_400_BAD_REQUEST)