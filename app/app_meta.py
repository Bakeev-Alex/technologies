from django.conf.urls import url
from objectpack import desktop
from .controller import controller

from .ui import ContentTypeActionPack
from .actions import ContentTypePack


def register_urlpatterns():
    """
    Регистрация урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экш паков
    """
    return controller.packs.extend(
        [ContentTypePack]
    )


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
    