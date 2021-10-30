from django.conf.urls import url
from objectpack import desktop
from .controller import controller

from .actions import ContentTypePack, UserPack, GroupPack, PermissionPack


def register_urlpatterns():
    """
    Регистрация урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экш паков
    """
    content_pack = ContentTypePack()
    user = UserPack()
    group = GroupPack()
    permission = PermissionPack()

    return controller.packs.extend(
        [content_pack, user, group, permission]
    )


def register_desktop_menu():
    """
    Регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
    