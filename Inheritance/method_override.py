name = input("Please enter your name: ")
age = int(input("How old are you? "))
hair_colour = input("What is your hair colour? ")
eye_colour = input("What colour are your eyes? ")

class Adult():
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_color = eye_colour
        self.hair_color = hair_colour

    def can_drive(self):
        print(f"Name: {self.name}")
        if age >= 18:
            print("{self.name} is old enough to drive")

class Child(Adult):

    def can_drive(self):
        print(f"Name: {self.name}")
        if age <= 18:
            print("{self.name} is not old enough to drive")

age_drive = Child()
age_drive.can_drive()