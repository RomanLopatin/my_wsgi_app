from front import routes, fronts
from my_wsgi_framework import Application

application = Application(routes, fronts)
