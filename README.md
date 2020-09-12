# Django Rest Framework Application

GET: http://127.0.0.1:8000/api/musicians/

GET: http://127.0.0.1:8000/api/albums/

POST: http://127.0.0.1:8000/api/musicians/


Test Data :
{
    "first_name": "ganesh",
    "last_name": "xeno",
    "instrument": "Guitar",
    "album_musician": [
        {
            "name": "NEO",
            "release_date": "2017-07-07",
            "num_stars": 5
        },
        {
            "name": "NEO 2",
            "release_date": "2017-07-22",
            "num_stars": 4
        }
    ]
}

admin: kuntal
pass: 12345


# DRF Filtering 
s1: s2: http://127.0.0.1:8000/api/search/

s2: http://127.0.0.1:8000/api/search/Kuntal/

s3: http://127.0.0.1:8000/api/search/?name=Kuntal

s4: http://127.0.0.1:8000/api/filter/backend/?search=kun



# Swagger
http://127.0.0.1:8000/swagger/

Note**: Perfer to use generics 

# Ref Docs
https://drf-yasg.readthedocs.io/en/stable

# JWT 
https://pypi.org/project/djangorestframework-simplejwt

# JSON API
https://pypi.org/project/djangorestframework-jsonapi/



# For testing uncomment code in views, models, urls, serialzer, the test below
http://127.0.0.1:8000/api/musicians/
http://127.0.0.1:8000/api/musicians/search1/
http://127.0.0.1:8000/api/musicians/search2/kuntal/
http://127.0.0.1:8000/api/musicians/search3/?name=kuntal
http://127.0.0.1:8000/api/filter/backend/?search=ku
