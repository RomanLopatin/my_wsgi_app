from datetime import date

from views import IndexView, HiView, Hello

routes = {
    '/': IndexView(),
    '/hi/': HiView(),
    '/hello/': Hello()
}


# Front controllers
def data_front(request):
    request['data'] = date.today()


def secret_front(request):
    request['secret'] = 'some secret'


def other_front(request):
    request['key'] = 'key'


fronts = [data_front, secret_front, other_front]