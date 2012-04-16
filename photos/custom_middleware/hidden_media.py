
from django.conf import settings
from django import http
from django.utils.log import getLogger
from django.conf import settings

logger = getLogger('django.request')

class HiddenMediaMiddleware(object):
    """
    'HiddenMedia' middleware for preventing http access to media files:

    """

    def process_request(self, request):
        """
        This will check for a valid media cookie value. If the cookie
        is not valid it will return a forbidden error.
        """
        if request.path.startswith(settings.MEDIA_URL) and not request.get_signed_cookie('test_cookie', False, max_age=1):
            return http.HttpResponseForbidden('<h1>Forbidden</h1>')

