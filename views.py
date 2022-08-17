# page controller 1
from pprint import pprint

from my_wsgi_framework.templator import render


class IndexView:

    def __call__(self, request):

        data = request.get('data', None)
        return '200 OK', render('index.html', data=data, hero_list=[{'name': 'Hero 1'}, {'name': 'Hero 2'}])


# page controller 2
class HiView:

    def __call__(self, request):
        return '200 OK', 'Hi!'


# page controller 3
class Hello:

    def __call__(self, request):
        return '200 OK', '<h1>Hello!</h1>'
