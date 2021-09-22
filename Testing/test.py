done = False

#Boolean
while not done:
    quit = input("Do you want to quit? ")
    if quit.lower() == "y":
        done = True
        print("Bye!")

    if not done:
        attack = input("Do you want to attack the dragon? ")
        if attack.lower() == "y":
            done = True
            print("Bad choice, you died!")


def count_up(start, end):
    for current_number in range(start, end + 1):
        print(current_number)

count_up(5, 10)
