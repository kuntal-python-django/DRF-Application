from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Post)
