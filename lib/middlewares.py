from pprint import pprint
from  django.middleware.csrf import CsrfViewMiddleware

class middleware_factory:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        resp = self.get_response(request)
        content = resp.content.decode('utf-8')
        resp.content = content.replace('Titulo da Página', 'Novo Titulo').encode('utf-8')
        return resp
