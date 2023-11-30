from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.crypto import get_random_string
from django.urls import reverse
from random import randint 



class MyTokenObtainView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Couldn't create a new token for the user"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLogout(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User is not logged in"}, status=status.HTTP_400_BAD_REQUEST)



class UserRegister(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            cd = serializer.validated_data
            random_code = randint(100000, 999999)
            # SMS.verification({
            #     'reseptor' : cd['phone'],
            #     'template' : 'template_name',
            #     'type' : '1',
            #     'param1' : random_code
            #     })
            token = get_random_string(length=100)
            Otp.objects.create(email=cd['email'], phone=cd['phone'], password=cd['password'],
                               full_name=cd['full_name'], type=cd['type'], otp_code=random_code, token=token)

            return Response({'token': token}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCheckOtp(APIView):
    def post(self, request):
        serializer = UserCheckOtp(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PasswordChange(APIView):
    def put(self, request):
        serializer = serializer.PasswordChangeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            if serializer.validated_data['new_password'] == serializer.validated_data['confirm_new_password']:
                serializer.save()
                return Response({"detail": "Password changed successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "New passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


