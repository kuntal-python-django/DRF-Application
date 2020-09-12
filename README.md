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



HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
HTTP_208_ALREADY_REPORTED
HTTP_226_IM_USED

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
HTTP_308_PERMANENT_REDIRECT

HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_426_UPGRADE_REQUIRED
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_506_VARIANT_ALSO_NEGOTIATES
HTTP_507_INSUFFICIENT_STORAGE
HTTP_508_LOOP_DETECTED
HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
HTTP_510_NOT_EXTENDED
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED

https://www.django-rest-framework.org/api-guide/status-codes/
