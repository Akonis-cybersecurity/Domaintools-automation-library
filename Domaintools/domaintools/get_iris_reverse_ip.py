from sekoia_automation.action import Action
from .models import BaseDomaintoolsAction


class DomaintoolsIrisReverseIP(BaseDomaintoolsAction, Action):
    action_name = "iris_reverse_ip"
