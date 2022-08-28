class RoomExit(object):
    def __init__(self, direction, description, status=None, linksTo="", condition=None):
        self.direction = direction
        self.description = description
        self.status = status
        self.linksTo = linksTo
        self.condition = condition
