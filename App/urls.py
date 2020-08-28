from django.urls import path

from .views import *

urlpatterns = [
    
    # swagger testing
    path('api/musicians/', MusicianListView.as_view()),
    path('api/albums/', AlbumListView.as_view()),
    # custom doc swagger
    path('api/users/', CreateUSer.as_view()),
    # filter
    path('api/search/', FilterUserDemo3.as_view()),
    path('api/search/<str:name>/', FilterUserDemo2.as_view()),
    path('api/filter/backend/', FilterUserDemo4.as_view()),

]