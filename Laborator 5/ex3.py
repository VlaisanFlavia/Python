class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


def calculate_mileage():
    return 30


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()} - {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        return f"{super().display_info()} - {self.num_wheels} wheels"

    def calculate_mileage(self):
        return 50


class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def display_info(self):
        return f"{super().display_info()} - Towing Capacity: {self.towing_capacity} lbs"

    def calculate_towing_capacity(self):
        return self.towing_capacity


car = Car(make="Toyota", model="Camry", year=2022, num_doors=4)
print(car.display_info())
print("Mileage:", calculate_mileage())

motorcycle = Motorcycle(make="Harley-Davidson", model="Street 750", year=2022, num_wheels=2)
print(motorcycle.display_info())
print("Mileage:", motorcycle.calculate_mileage())

truck = Truck(make="Ford", model="F-150", year=2022, towing_capacity=10000)
print(truck.display_info())
print("Towing Capacity:", truck.calculate_towing_capacity())
