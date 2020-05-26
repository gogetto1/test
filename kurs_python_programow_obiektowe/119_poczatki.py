class User:
    age = 0
    name = ""
    def __init__(self, age, name):
        print("Jestem inicjalizatorem")
        self.age = age
        self.name = name

        self.ageInFuture = age + 1

    def print_age(self, message):
        print(message, "wiek", self.age, self.name)



user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age("dodatkowy tekst troche inny")
user2.print_age("tekst")

print(user1.ageInFuture)