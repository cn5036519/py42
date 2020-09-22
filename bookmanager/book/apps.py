from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    # 在admin管理后台显示的应用名称
    verbose_name = "图书"
