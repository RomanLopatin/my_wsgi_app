from wsgiref.util import setup_testing_defaults


# from run import not_found_404_view
def not_found_404_view(request):
    # print(request)
    return '404 WHAT', '404 PAGE Not Found'


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        setup_testing_defaults(environ)
        path = environ['PATH_INFO']
        # print(path)
        # path.lower()
        # print(path)
        if not path.endswith('/'):
            path = f'{path.lower()}/'
        if path in self.routes:
            view = self.routes[path]
        else:
            view = not_found_404_view
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        print(type(body))

        return [body.encode('utf-8')]




