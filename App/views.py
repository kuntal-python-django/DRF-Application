from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
from .models import *
from .serializers import *
# rest_framework
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



class MusicianListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    # authentication_classes =[]  # to bypass security
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class AlbumListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# custom Request & Response in swagger
class CreateUSer(APIView):
    permission_classes = [AllowAny, ]

    response = openapi.Response(
        'response description', CreateUserResponseSerializers
    )
    
    @swagger_auto_schema(
        request_body = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='User Name'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User Email'),
            },
            required=['email'],
        ),

        responses = {
            status.HTTP_200_OK: CreateUserResponseSerializers
        } 
    )

    def post(self, request, format=None):
        name = request.data['name']
        email = request.data['email']
        print(name, email)

        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)



