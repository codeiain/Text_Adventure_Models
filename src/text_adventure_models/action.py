class Action(object):
    def __init__(self, action, target, description, status=None):
        self.action = action
        self.target = target
        self.description = description
        self.status = status
