from django.utils.deprecation import MiddlewareMixin

class CrossDomain(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origi'] = '*'
        return response