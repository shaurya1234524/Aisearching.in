from django.http import HttpResponsePermanentRedirect

class TrailingSlashMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the path doesn't have a trailing slash and it's not the admin page
        if not request.path.endswith('/') and not request.path.startswith('/admin'):
            return HttpResponsePermanentRedirect(request.path + '/')
        
        response = self.get_response(request)
        return response
