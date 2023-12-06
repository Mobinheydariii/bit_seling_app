from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
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

    

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    password = serializers.CharField(required=True, validators=[validate_password])



class SimpleUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleUser
        fields = "__all__"



class SimpleUserRegistertionSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)

    password = serializers.CharField(read_only=True,
                                        validators=[validate_password])
    password2 = serializers.CharField(read_only=True)


    class Meta:
        model = SimpleUser
        fields = ('phone', 'email', 'username', 'password', 'password2')

