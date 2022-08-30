from .conditions import Condition

class Description(object):
    def __init__(self, text, condition):
        self.text = text
        self.condition = condition

    def get_description(self):
        if Condition(str(self.condition)) is Condition.NONE:
            return self.description
