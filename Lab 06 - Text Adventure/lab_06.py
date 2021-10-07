class Room:
    """
    This is the class that represents the building
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("Foyer", None, 1, 6, None)
    room_list.append(room)

    room = Room("Dining", None, None, 2, 0)
    room_list.append(room)

    room = Room("Hall", 1, None, 3, 6)
    room_list.append(room)

    room = Room("Kitchen", 2, 7, None, None)
    room_list.append(room)

    room = Room("Main Bedroom", 6, None, None, 5)
    room_list.append(room)

    room = Room("Bathroom", None, 4, None, None)
    room_list.append(room)

    room = Room("Hallway", 0, 2, 4, None)
    room_list.append(room)

    room = Room("Basement", None, None, 3, None)
    room_list.append(room)

    current_room = 0
    print(room_list[current_room].description)
    print()

    done = False



main()
