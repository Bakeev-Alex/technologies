from objectpack.actions import ObjectPack
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from objectpack.ui import ModelEditWindow


class ContentTypePack(ObjectPack):

    model = ContentType

    add_to_menu = True

