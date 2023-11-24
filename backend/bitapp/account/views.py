from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import UserSerializer
from .models import (
    User,
    Singer,
    Producer,
    Musician,
    Supporter,
    SimpleUser
)




class OfficialProducerAPIList(APIView):
    def get(self, request):
        producers = Producer.official.all()
        serializer = UserSerializer(producers, many=True)
        return Response(data=serializer.data, status=200)
        