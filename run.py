from front import routes, fronts
from my_wsgi_framework import Application
from wsgiref.simple_server import make_server

application = Application(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
