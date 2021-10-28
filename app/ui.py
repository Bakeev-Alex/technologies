from m3.actions import Action, ActionPack
from m3.actions.results import OperationResult

from .actions import ContentTypePack


class ContentTypeAction(Action):
    url = 'inner'

    def run(self, request, context):
        return OperationResult(message='Test okey')


class ContentTypeActionPack(ActionPack):
    def __init__(self):
        super(ContentTypeActionPack, self).__init__()
        self.actions.extend([ContentTypeAction])
        self.subpacks.append([ContentTypePack])


# class InnerActionPack(ActionPack):
#     url = 'inner'
#
#     def __init__(self):
#         super(InnerActionPack, self).__init__()
#         self.actions.extend([ContentTypeAction])

