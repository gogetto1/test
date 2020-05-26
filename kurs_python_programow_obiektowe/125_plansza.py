from random import randint


class Rocket:

    def __init__(self, speed=1):
        self.altitude = 0

        self.speed = speed

    def moveUp(self):

        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)


rockets = [Rocket(randint(1, 6)) for _ in range(5)]

for _ in range(10):
    rocketIndexToMove = randint(0, 4)
    rockets[rocketIndexToMove].moveUp()


for rocket in rockets:
    print(rocket.altitude)

