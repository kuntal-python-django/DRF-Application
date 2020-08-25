from django.urls import path

from .views import *

urlpatterns = [
    
    path('api/musicians/', MusicianListView.as_view()),
    path('api/musicians/(?P<pk>\d+)/', MusicianView.as_view()),
    path('api/albums/', AlbumListView.as_view()),
    path('api/albums/(?P<pk>\d+)/', AlbumView.as_view()),

]