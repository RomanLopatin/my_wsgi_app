from my_wsgi_framework.templator import render
from patterns.creational_patterns import Engine, Logger

site = Engine()
logger = Logger('main')


class IndexView:

    def __call__(self, request):
        data = request.get('data_of_today', None)
        return '200 OK', render('index.html', data=data, hero_list=[{'name': 'Hero 1'}, {'name': 'Hero 2'}])


class CategoryCreate:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            category_name = data['category_name']
            category_name = site.decode_value(category_name)

            #
            logger.log(f'Создаем категорию {category_name}')
            #
            new_category = site.create_category(category_name)
            site.categories.append(new_category)

            return '200 OK', render('category-list.html', category_list=site.categories)
        else:
            print('We are here!')
            print(request['request_params'])
            return '200 OK', render('category-create.html')


class CategoryListView:

    def __call__(self, request):
        return '200 OK', render('category-list.html', category_list=site.categories)


class CourseCreate:

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            course_name = data['course_name']
            course_name = site.decode_value(course_name)
            #
            logger.log(f'Создаем курс {course_name}')
            #
            self.category_id = int(request['request_params']['id'])
            category = site.find_category_by_id(int(self.category_id))

            new_course = site.create_course(course_name, category)
            site.courses.append(new_course)
            category.courses.append(new_course)

            return '200 OK', render('course-list.html', course_list=category.courses, cat_id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('course-create.html', cat_name=category.name, cat_id=category.id)
            except KeyError:
                return '200 OK', 'No categories have been added yet'


class CourseListView:

    def __call__(self, request):
        try:
            # print(f"ID: {int(request['request_params']['id'])}")
            category = site.find_category_by_id(int(request['request_params']['id']))
            return '200 OK', render('course-list.html', course_list=category.courses, cat_name=category.name,
                                    cat_id=category.id)
        except KeyError:
            return '200 OK', 'No courses have been added yet'


class ContactView:

    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            title = data['title']
            text = data['text']
            email = data['email']
            print('method: Post')
            print(f'Сообщение!')
            print(f'Email: {email}')
            print(f'Title: {title}')
            print(f'Text: \n {text}')
            return '200 OK', render('Thanks.html')
        else:
            print(request['request_params'])
            return '200 OK', render('contact.html')
