from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import login
from .models import *
  

        

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
       return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['full_name'] = user.profile.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['bio'] = user.profile.bio
        token['image'] = str(user.profile.image)
        # ...
        return token
    

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    user_name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    type = serializers.CharField(required=True)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'type', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        if not (8 <= len(data['password_conf']) <= 16):
            raise serializers.ValidationError("Password is smaler than 8 or biger than 16")
        return data
    

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            type=validated_data['type']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    


class UserCheckOtp(serializers.Serializer):
    otp = serializers.CharField(max_length=4)

    def validate(self, data):
        token = self.context['request'].GET.get('token')
        otp = Otp.objects.get(otp=data['otp'], token=token)
        if otp:
            user = User.objects.create_user(email=otp.email, phone=otp.phone, user_name=otp.user_name, type=otp.type, password=otp.password_conf)
            login(self.context['request'], user)
        else:
            raise serializers.ValidationError("Invalid otp code")