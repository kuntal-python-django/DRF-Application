from django.urls import path

from .views import *

urlpatterns = [
    
    path('api/musicians/', MusicianListView.as_view()),
    path('api/albums/', AlbumListView.as_view()),
    path('api/users/', CreateUSer.as_view()),

]