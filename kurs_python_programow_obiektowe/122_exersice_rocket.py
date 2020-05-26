from random import randint


class Rocket:
    def __init__(self):
        self.altitude = 0

    def moveUp(self):
        self.altitude += 1


rockets = [Rocket() for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].moveUp()


for rocket in rockets:
    print(rocket.altitude)
