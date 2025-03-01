# paola Vazquez
# worked on march 28 , 2025
# Problem 6: Modify the Car class with additional attributes


class Car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color
    
    def get_type(self):
        return self.car_type
    
    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.model} {self.year} {self.color} {self.car_type}"

# Get user input for car details
model = input("Enter the car model: ")
year = input("Enter the car year: ")
color = input("Enter the car color: ")
car_type = input("Enter the car type (e.g., Sedan, SUV, Coupe): ")
manufacturer = input("Enter the car manufacturer: ")

# Create car object with user input
user_car = Car(model, year, color, car_type, manufacturer)

# Print car details
print("\nCar Details:")
print(f"Model: {user_car.get_model()}")
print(f"Year: {user_car.get_year()}")
print(f"Color: {user_car.get_color()}")
print(f"Type: {user_car.get_type()}")
print(f"Manufacturer: {user_car.get_manufacturer()}")
print(f"Full Specs: {user_car.fullspecs()}")
