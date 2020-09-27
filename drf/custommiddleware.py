from datetime import datetime, timedelta
from django.core.cache import cache
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class KuntalDemoMiddleware(MiddlewareMixin):
    def process_request(self, request):
        cache.set('xxx', 11111)
        print("###############################")
        print('\n', '          My Middleware         ', '\n')
        print("###############################")
