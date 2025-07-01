class Car: # creating a class
    def __init__(self, brand, fuel_type):
        # constructor (__init__) initializes the car's brand and fuel type
        self.brand = brand
        self.fuel_type = fuel_type

    def drive(self, distance: float):
        # method to simulate driving the car a certain distance
        print(f'Driving {self.brand} for {distance} km [{self.fuel_type}]')

# creating an instance of Car (Volvo)
volvo: Car = Car(brand='Volvo', fuel_type='Diesel')
# creating a second instance of Car (BMW)
bmw: Car = Car(brand='BMW', fuel_type='Electric')

# printing the brand and fuel type of each car
print(volvo.brand, "->", volvo.fuel_type)
print(bmw.brand, "->", bmw.fuel_type, "\n")

# calling the drive method using Volvo instance
# simulating driving the Volvo for 10km
volvo.drive(distance=10)