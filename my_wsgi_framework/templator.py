from jinja2 import Template
import os

from settings import TEMPLATE_FOLDER, BASE_DIR


def render(template_name, template_folder=TEMPLATE_FOLDER, **kwargs):
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

