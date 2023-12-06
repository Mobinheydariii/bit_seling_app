from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.crypto import get_random_string
from rest_framework import generics
from random import randint 

from .serializers import *



class UserList(APIView):
    def get(self, request):
        instance = User.objects.all()
        serializer = UserSerializer(instance=instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class UserPanel(APIView):
    def get(self, request, user_name):
        instance = User.objects.get(user_name=user_name)
        if request.user == instance:
            serializer = UserSerializer(instance=instance)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "You don't have permission to view this profile."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, user_name):
        instance = User.objects.get(user_name=user_name)
        if request.user != instance:
            return Response({"error":"You don't have permission to edit this profile"},status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        serializer = UserSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        

class UserProfile(APIView):
    def get(self, request, user_name):
        user = User.objects.get(user_name=user_name)
        profile = UserProfile.options.get(user=user)
        serializer = UserSerializer(instance=profile)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user is not None:
                login(request, user)
                token = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
class UserLogout(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User is not logged in"}, status=status.HTTP_400_BAD_REQUEST)



class SimleUserRegisterView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response({"detail": "You are authenticated"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = SimpleUserRegistertionSerializer(data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user = User.objects.create(
                    phone = serializer.validated_data['phone'],
                    email = serializer.validated_data['email'],
                    username = serializer.validated_data['username'],
                    password = serializer.validated_data['password'],
                    type = "Simple_user"
                )
                user.save()
                
                return Response("user created")
                
            else:
                return Response({"errores" : serializer.errors})
