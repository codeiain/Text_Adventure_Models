class Location(object):
    def __init__(self, id, name, descriptions, point_of_intrests, exits=None):
        self.id = id
        self.name = name
        self.descriptions = descriptions
        self.point_of_intrests = point_of_intrests
        self.exits = exits

    def get_description(self):
        description_string = ""
        for description in self.descriptions:
            description_string += description.get_description()
        for poi in self.point_of_intrests:
            description_string += poi.get_description()
        for room_exit in self.exits:
            description_string += room_exit.get_description()

        return description_string
