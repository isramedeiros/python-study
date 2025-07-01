class Car:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def drive(self, distance: float):
        print(f'Driving {self.brand} for {distance} km [{self.fuel_type}]')

volvo: Car = Car(brand='Volvo', fuel_type='Diesel')
bmw: Car = Car(brand='BMW', fuel_type='Electric')

print(volvo.brand, "->", volvo.fuel_type)
print(bmw.brand, "->", bmw.fuel_type, "\n")

volvo.drive(distance=10)