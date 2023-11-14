class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        return f"{self.name} is giving birth."


class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying."


class Fish(Animal):
    def __init__(self, name, species, scale_color):
        super().__init__(name, species)
        self.scale_color = scale_color

    def swim(self):
        return f"{self.name} is swimming."


mammal = Mammal(name="Lion", species="Panthera leo", fur_color="Golden")
print(mammal.give_birth())
print(f"{mammal.name} has fur color: {mammal.fur_color}")

bird = Bird(name="Eagle", species="Aquila chrysaetos", wingspan=6.5)
print(bird.fly())
print(f"{bird.name} has wingspan: {bird.wingspan} feet")

fish = Fish(name="Clownfish", species="Amphiprioninae", scale_color="Orange")
print(fish.swim())
print(f"{fish.name} has scale color: {fish.scale_color}")
