from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView, Response
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
        serializer = UserSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"errors":serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        

class UserDetail(APIView):
    def get(self, request, user_name):
        instance = User.objects.get(user_name=user_name)
        serializer = UserSerializer(instance=instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.authenticate()
            if user is not None:
                login(request, user)
                return Response({"detail": "Logged in successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def logout(self, request):
    logout(request.user)
    return HttpResponseRedirect('/')
                        

        