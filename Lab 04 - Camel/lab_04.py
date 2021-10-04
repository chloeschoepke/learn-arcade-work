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

        choice_options()
        choice = input("What is your choice? ")

        # choice quit
        if choice.upper() == "Q":
            done = True
            print("You have successfully ended your adventure!")

        # choice status check
        elif choice.upper() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in Hydroflask:", hydroflask)
            security_behind = miles_traveled - security_traveled
            print("Security is", security_behind, "miles behind you.")

        # choice break
        elif choice.upper() == "D":
            elephant_tiredness = 0
            print("The elephant is happy!")
            security_traveled += random.randrange(7, 14)

        # choice full speed
        elif choice.upper() == "C":
            full_speed = random.randrange(10, 20)
            print("You traveled ", full_speed, "miles!")
            miles_traveled += full_speed
            thirst += 1
            elephant_tiredness += random.randrange(1, 3)
            security_traveled += random.randrange(7, 14)
            oasis = random.randrange(1, 20)
            # five is my lucky number
            if oasis == 5 and not done:
                elephant_tiredness = 0
                thirst = 0
                hydroflask = 0
                print("You found a bar!")
                print("After you impressed the owner with your elephant, "
                      "he refilled your Hydroflask and gave the elephant a snack!")

        # choice moderate speed
        elif choice.upper() == "B":
            moderate_speed = random.randrange(5, 12)
            print("You traveled ", moderate_speed, "miles!")
            miles_traveled += moderate_speed
            thirst += 1
            elephant_tiredness += 1
            security_traveled += random.randrange(7, 12)
            oasis = random.randrange(1, 20)
            # five is my lucky number
            if oasis == 5 and not done:
                elephant_tiredness = 0
                thirst = 0
                hydroflask = 0
                print("You found a bar!")
                print("After you impressed the owner with your elephant, "
                      "he refilled your Hydroflask and gave the elephant a snack!")

        # choice drink
        elif choice.upper() == "A":
            if hydroflask == 0:
                print("There are no more drinks left")

            else:
                hydroflask -= 1
                thirst = 0
                print("You have", hydroflask, "drinks left, way to hydrate!")

        if thirst > 4 and thirst <= 6 and not done:
            print("You are thirsty!")

        if thirst > 6:
            print("You died of thirst!")
            done = True

        if elephant_tiredness > 5 and elephant_tiredness <= 8 and not done:
            print("Your elephant is tired!")

        if elephant_tiredness > 8:
            print("The elephant collapsed in exhaustion.")
            done = True

        if security_behind <= 0:
            print("Security caught you and the elephant has been confiscated")
            print("Maybe you'll make it next time")
            done = True

        if security_behind <= 15:
            print("Security is getting close!")

        if miles_traveled >= 200 and not done:
            print("You have successfully made it home and acquired a new pet, congrats!")




main()
