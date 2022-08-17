from front import routes, fronts
from my_wsgi_framework.simple_wsgi_app import Application

application = Application(routes, fronts)
