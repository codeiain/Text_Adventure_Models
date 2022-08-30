from .conditions import Condition

class PointOfIntrest(object):
    def __init__(
        self, poi_type, target, condition, description, direction=None, linkto=None
    ):
        self.type = poi_type
        self.target = target
        self.condition = condition
        self.description = description
        self.direction = direction
        self.linkto = linkto

    def get_description(self):
        if self.condition is Condition.NONE:
            return self.description
        else:
            return ""
