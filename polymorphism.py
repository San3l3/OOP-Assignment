class Animal:
    def move(self):
        print("This animal moves in some way.")


class Dog(Animal):
    def move(self):
        print("The dog runs swiftly. 🐕")


class Snake(Animal):
    def move(self):
        print("The snake slithers silently. 🐍")


class Bird(Animal):
    def move(self):
        print("The bird soars through the sky. 🐦")


# Polymorphism in action
animals = [Dog(), Snake(), Bird()]

for animal in animals:
    animal.move()
