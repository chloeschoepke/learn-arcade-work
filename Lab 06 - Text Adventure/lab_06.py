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
    done = False

    room_list = []
    # Room 0 Foyer
    room = Room("You are in the foyer. "
                "There is a hallway to the south and a door to the east.", None, 1, 6, None)
    room_list.append(room)
    # Room 1 Dining Room
    room = Room("You have entered the dining room. "
                "You can return to the foyer to the west, or enter the hall to the south.", None, None, 2, 0)
    room_list.append(room)
    # Room 2 Hall
    room = Room("You are in the hall. "
                "To your north and south are doors, or continue down the hallway to the west.", 1, None, 3, 6)
    room_list.append(room)
    # Room 3 Kitchen
    room = Room("You stand in the kitchen. "
                "You can go north towards the hall, or enter the pantry door to the east.", 2, 7, None, None)
    room_list.append(room)
    # Room 4 Main Bedroom
    room = Room("You have reached the main bedroom. "
                "To the north is the hallway, to the west is a door to what seems to be a bathroom.", 6, None, None, 5)
    room_list.append(room)
    # Room 5 Bathroom
    room = Room("You are in the bathroom. "
                "Return east to return to the bedroom.", None, 4, None, None)
    room_list.append(room)
    # Room 6 Hall
    room = Room("You stand in the hallway. "
                "To your north is the foyer and to the south is the bedroom. "
                "You can enter one of the doors or continue down the hall to the east.", 0, 2, 4, None)
    room_list.append(room)
    # Room 7 Basement
    room = Room("You have entered the pantry to find a set of stairs leading to the basement. "
                "You can return to the kitchen to the west.", None, None, 3, None)
    room_list.append(room)

    while not done:

        done = False
        current_room = 0
        print()
        print(room_list[current_room].description)
        choice = input("What will you do? ")

        if choice.upper() == "QUIT":
            print("Thank you for playing")
            done = True

        # User chose to go north
        if choice.upper() == "N" or "NORTH":
            next_room = room_list[current_room].north
            if next_room is None and not done:
                print("You cannot go that way!")
            else:
                current_room = next_room

        # User chose to go east
        elif choice.upper() == "E" or "EAST":
            next_room = room_list[current_room].east
            if next_room is None and not done:
                print("You cannot go that way!")
            else:
                current_room = next_room

        # User chose to go south
        elif choice.upper() == "S" or "SOUTH":
            next_room = room_list[current_room].south
            if next_room is None and not done:
                print("You cannot go that way!")
            else:
                current_room = next_room

        # User chose to go west
        elif choice.upper() == "W" or "WEST":
            next_room = room_list[current_room].west
            if next_room is None and not done:
                print("You cannot go that way!")
            else:
                current_room = next_room

        # Program doesn't understand
        else:
            print("I don't understand what you are saying, please try something else.")



main()
