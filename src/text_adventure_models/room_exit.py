from conditions import Condition

class RoomExit(object):
    def __init__(self, direction, description, linksTo="", condition=None, target=None):
        self.direction = direction
        self.description = description
        self.linksTo = linksTo
        self.condition = condition
        self.target = target

    def get_description(self):
        if Condition(str(self.condition)) is Condition.NONE:
            return self.description
