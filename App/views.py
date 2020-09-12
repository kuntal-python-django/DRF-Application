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
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
# swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Get and Post
class MusicianListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    # authentication_classes =[]  # to bypass security
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# Get and Post
class AlbumListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# data Filtering
class FilterUserDemo1(generics.ListAPIView):
    serializer_class = UserListingSerializer

    # Filtering on know params
    def get_queryset(self):
        return User.objects.filter(name='kuntal')

    
class FilterUserDemo2(generics.ListAPIView):
    serializer_class = UserListingSerializer

    # Filtering on kwarg which we are getting from url
    def get_queryset(self):
        kwarg_url_value = self.kwargs['name']
        return User.objects.filter(name=kwarg_url_value)
    
    
class FilterUserDemo3(generics.ListAPIView):
    serializer_class = UserListingSerializer
    
    # Filtering url query params
    def get_queryset(self):
        queryset = User.objects.all()
        q_value = self.request.query_params.get('name', 'None')
        if q_value is not None:
            queryset = queryset.filter(name=q_value)
        return queryset


# drf search fields
# patter match work here
class FilterUserDemo4(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']




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



"""
# to practise uncomment here

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
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import filters


# Get and Post
class MusicianListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# Post
class MusicianPOSTView(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# Get All
class MusicianGETView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# Retrieve one data
class MusicianRetrieveAPIViewView(generics.RetrieveAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# Update one
class MusicianUPDATEView(generics.UpdateAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


# delete one
class MusicianDeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny, ]
    lookup_field = 'id'
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class FilterUserDemo1(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MusicianSerializer
    # Filtering on know params
    def get_queryset(self):
        queryset = Musician.objects.filter(instrument='m3')
        return queryset


class FilterUserDemo2(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MusicianSerializer
    # Filtering on kwarg which we are getting from url
    def get_queryset(self):
        kwarg_url_value = self.kwargs['first_name']
        return Musician.objects.filter(first_name=kwarg_url_value)


class FilterUserDemo3(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MusicianSerializer
    # Filtering url query params
    def get_queryset(self):
        queryset = Musician.objects.all()
        q_value = self.request.query_params.get('name', 'None')
        if q_value is not None:
            queryset = queryset.filter(first_name=q_value)
        return queryset


# drf search fields
# patter match work here
class FilterUserDemo4(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'instrument']

"""
