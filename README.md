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


# Swagger
http://127.0.0.1:8000/swagger/

Note**: Perfer to use generics 

# Ref Docs
https://drf-yasg.readthedocs.io/en/stable

# JWT 
https://pypi.org/project/djangorestframework-simplejwt

# JSON API
https://pypi.org/project/djangorestframework-jsonapi/
