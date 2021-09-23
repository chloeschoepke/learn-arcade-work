import random

def welcome_message():
    print("Welcome to Zoo Escape!")
    print("You have stolen an elephant to make your way home from the Blank Park Zoo.")
    print("Security has been called and are chasing after you! Survive your travels")
    print("home and outrun security with your new pet.")


def choice_options():

    print("""Your choices are:
        A. Drink from your hydroflask.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for a break.
        E. Status check.
        Q. Quit.""")


def main():
    welcome_message()

    miles_traveled = 0
    security_traveled = -20
    hydroflask = 3
    thirst = 0
    elephant_tiredness = 0
    done = False

    while not done:
        security_behind = miles_traveled - security_traveled
        full_speed = random.randrange(10, 20)
        moderate_speed = random.randrange(5, 12)

        choice_options()
        choice = input("What is your choice? ")
        if choice.upper() == "Q":
            done = True
            print("You have successfully ended your adventure!")

        if choice.upper() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in Hydroflask:", hydroflask)
            print("Security is", security_behind, "miles behind you.")

        elif choice.upper() == "A":
            if hydroflask == 0:
                print("You have die-drated, should have tried hydrating more")
                done = True
            else:
                hydroflask -= 1
                thirst = 0
                print("You have", hydroflask, "drinks left, way to hydrate!")

        if choice.upper() == "D":
            elephant_tiredness = 0



main()
