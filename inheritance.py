# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def show_details(self):
        print(f"{self.name} from {self.universe} has the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")


# Subclass 1
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, flight_speed):
        super().__init__(name, power, universe)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} takes off and flies at {self.flight_speed} mph! ✈️")


# Subclass 2
class StrengthHero(Superhero):
    def __init__(self, name, power, universe, strength_level):
        super().__init__(name, power, universe)
        self.strength_level = strength_level

    def use_power(self):
        print(f"{self.name} lifts a building with strength level {self.strength_level}! 💪")


# Example usage
hero1 = FlyingHero("SkyBlazer", "Flight", "Skyverse", 500)
hero2 = StrengthHero("Titan", "Super Strength", "EarthPrime", 9000)

hero1.show_details()
hero1.use_power()

hero2.show_details()
hero2.use_power()
