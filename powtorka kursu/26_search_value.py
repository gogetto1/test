import random


searchValue = random.randint(0, 100)
userValue = None

while userValue != searchValue:
    userValue = int(input("Input your value from zero to one hundred: "))
    if userValue > searchValue:
        print("You value is BIGGER than searching number")

    elif userValue < searchValue:
        print("You value is SMALLER than searching number")

    else:
        print("Great!That was:", searchValue, "You find it!!!")
