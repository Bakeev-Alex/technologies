from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from m3.actions.exceptions import ApplicationLogicException

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from .ui import PermissionWindow, UserWindow


class ContentTypePack(ObjectPack):

    model = ContentType
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=model)


class UserPack(ObjectPack):

    model = User
    add_to_menu = True
    # add_window = edit_window = ModelEditWindow.fabricate(model=model)
    add_window = edit_window = UserWindow


class GroupPack(ObjectPack):

    model = Group
    add_to_menu = True
    add_window = edit_window = ModelEditWindow.fabricate(model=model)


class PermissionPack(ObjectPack):
    model = Permission
    add_to_menu = True

    add_window = edit_window = PermissionWindow

    # FixMe: При попытки вывести, через .fabricate выдает
    #  ошибку AssertionError: Cant find pack for field content_type (realated model ContentType)
    # add_window = edit_window = ModelEditWindow.fabricate(model=model)
