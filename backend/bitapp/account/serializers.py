from rest_framework import serializers
from rest_framework.validators import UniqueValidator
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


class Singerserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Singer
        fields = "__all__"

        def create(self, validated_data):
            return Singer.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.artist_name = validated_data.get('artist_name', instance.artist_name)
            instance.save()
            return instance
class ProducerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producer
        fields = "__all__"
    
    def create(self, validated_data):
       return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.artist_name = validated_data.get('artist_name', instance.artist_name)
        instance.persentage = validated_data.get('persentage', instance.persentage)
        instance.save()
        return instance


class MusicianSerializer(serializers.SerializerMetaclass):

    class Meta:
        model = Musician
        fields = "__all__"


        def create(self, validated_data):
            return Musician.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.artist_name = validated_data.get('artist_name', instance.artist_name)
            instance.persentage = validated_data.get('persentage', instance.persentage)
            instance.save()
            return instance
        

class SupporterSeializer(serializers.ModelSerializer):

    class Meta:
        model = Supporter
        fields = '__all__'


        def create(self, validated_data):
            return Supporter.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
            instance.supporter_id = validated_data.get('supporter_id', instance.supporter_id)
            instance.supporter_password = validated_data.get('supporter_password', instance.supporter_password)
            instance.save()
            return instance




class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    phone = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    type = serializers.CharField(required=True)

    f_name = serializers.CharField()
    l_name = serializers.CharField()

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'password', 'password2', 'f_name', 'l_name', 'type')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'type':{'required':True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            f_name=validated_data['first_name'],
            l_name=validated_data['last_name'],
            type=validated_data['type']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])