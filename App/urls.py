from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # Auth
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
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







"""
# to practise uncomment here

from django.urls import path

from .views import *


urlpatterns = [
    path('api/musicians/', MusicianListView.as_view()),
    path('api/musicians/get/', MusicianGETView.as_view()),
    path('api/musicians/post/', MusicianPOSTView.as_view()),
    path('api/musicians/find/<int:id>/', MusicianRetrieveAPIViewView.as_view()),
    path('api/musicians/update/<int:id>/', MusicianUPDATEView.as_view()),
    path('api/musicians/delete/<int:id>/', MusicianDeleteView.as_view()),


    path('api/musicians/search1/', FilterUserDemo1.as_view()),
    path('api/musicians/search2/<str:first_name>/', FilterUserDemo2.as_view()),    
    path('api/musicians/search3/', FilterUserDemo3.as_view()),    
    path('api/filter/backend/', FilterUserDemo4.as_view()),

]

"""



