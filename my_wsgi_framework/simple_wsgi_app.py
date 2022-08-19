from pprint import pprint
from wsgiref.util import setup_testing_defaults

from my_wsgi_framework.utils import not_found_404_view, get_wsgi_input_data, parse_wsgi_input_data, parse_input_data


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        # pprint(environ)
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path.lower()}/'

        if path in self.routes:
            view = self.routes[path]

        else:
            view = not_found_404_view

        # Метод запроса
        method = environ['REQUEST_METHOD']
        # Данные из тела запроса (POST-запрос)
        data = get_wsgi_input_data(environ)
        data = parse_wsgi_input_data(data)
        # Данные из параметра 'QUERY_STRING'(GET-запрос)
        query_string = environ['QUERY_STRING']
        request_params = parse_input_data(query_string)

        request = {
            'method': method,
            'data': data,
            'request_params': request_params
        }

        # front controller
        for front in self.fronts:
            front(request)

        code, body = view(request)

        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
