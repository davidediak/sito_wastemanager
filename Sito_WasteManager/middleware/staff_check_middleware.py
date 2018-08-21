from django.http import HttpResponseForbidden


class StaffCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        full_path = request.get_full_path()
        if full_path.startswith('/cms/') and not request.user.is_staff:
            return HttpResponseForbidden()

        response = self.get_response(request)
        return response