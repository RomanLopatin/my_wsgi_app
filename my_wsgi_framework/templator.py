from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import os

from settings import TEMPLATE_FOLDER, BASE_DIR


def render(template_name, folder=TEMPLATE_FOLDER, **kwargs):
    env = Environment()
    template_path = os.path.join(BASE_DIR, folder)
    print(template_path)
    env.loader = FileSystemLoader(template_path)
    template = env.get_template(template_name)
    return template.render(**kwargs)


def render_(template_name, template_folder=TEMPLATE_FOLDER, **kwargs):
    """
    :param template_name: имя шаблона
    :param template_folder: папка в которой ищем шаблон
    :param kwargs: параметры
    :return:
    """
    template_path = os.path.join(BASE_DIR, template_folder, template_name)
    print(template_path)
    # Открываем шаблон по имени
    with open(template_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)
