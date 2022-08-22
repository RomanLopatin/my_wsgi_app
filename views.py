from my_wsgi_framework.templator import render


class IndexView:

    def __call__(self, request):
        data = request.get('data_of_today', None)
        return '200 OK', render('index.html', data=data, hero_list=[{'name': 'Hero 1'}, {'name': 'Hero 2'}])


class HiView:

    def __call__(self, request):
        return '200 OK', 'Hi!'


class Hello:

    def __call__(self, request):
        return '200 OK', '<h1>Hello!</h1>'


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
