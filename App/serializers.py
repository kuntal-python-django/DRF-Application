from rest_framework import serializers, fields
from .models import *
from  drf_yasg import openapi


# Noraml Relation
'''
class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument')


class AlbumSerializer(serializers.ModelSerializer):
    artist = MusicianSerializer(read_only=True, many=False)
    
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')
'''


# Nested Relation

class AlbumSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars')


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(many=True)

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument', 'album_musician')

    def create(self, validated_data):
        albums_data = validated_data.pop('album_musician')
        musician = Musician.objects.create(**validated_data)
        for album_data in albums_data:
            Album.objects.create(artist=musician, **album_data)
        return musician

    def update(self, instance, validated_data):
        albums_data = validated_data.pop('album_musician')
        albums = (instance.album_musician).all()
        albums = list(albums)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.instrument = validated_data.get('instrument', instance.instrument)
        instance.save()

        for album_data in albums_data:
            album = albums.pop(0)
            album.name = album_data.get('name', album.name)
            album.release_date = album_data.get('release_date', album.release_date)
            album.num_stars = album_data.get('num_stars', album.num_stars)
            album.save()
        return instance


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']


# demo response serializer
class CreateUserResponseSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()


class UserListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
        



""" 
# to practise uncomment here

from rest_framework import serializers, fields
from .models import *


# Noraml Relation
class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument')

"""


