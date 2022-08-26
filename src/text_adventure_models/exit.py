class Exit(object):
    def __init__(self, direction, description, linksTo=""):
        self.direction = direction
        self.description = description
        self.linksTo = linksTo