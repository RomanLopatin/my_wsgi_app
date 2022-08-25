from datetime import date

from views import IndexView, CategoryCreate, CategoryListView, ContactView, CourseCreate, CourseListView

routes = {
    '/': IndexView(),
    '/category-create/': CategoryCreate(),
    '/category-list/': CategoryListView(),
    '/course-create/': CourseCreate(),
    '/course-list/': CourseListView(),
    '/contact/': ContactView()
}


# Front controllers
def data_front(request):
    request['data_of_today'] = date.today()


def secret_front(request):
    request['secret'] = 'some secret'


def other_front(request):
    request['key'] = 'key'


fronts = [data_front, secret_front, other_front]
