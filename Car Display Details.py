class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Example usage:
car_instance = Car(make="Toyota", model="Camry", year=2022)

# Display details of the car
car_instance.display_details()
