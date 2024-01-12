class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        # Default fare calculation: seating capacity * 100
        return self.capacity * 100

class Bus(Vehicle):
    def __init__(self, capacity):
        # Call the constructor of the base class (Vehicle)
        super().__init__(capacity)

    def calculate_fare(self):
        # Calculate the default fare using the base class method
        default_fare = super().calculate_fare()

        # Add an extra 10% on the full fare as a maintenance charge for Bus instances
        maintenance_charge = 0.1 * default_fare

        # Calculate the total fare for Bus instance
        total_fare = default_fare + maintenance_charge

        return total_fare

# Example usage:
bus_instance = Bus(capacity=50)

# Calculate and display the total fare for the Bus instance
total_fare = bus_instance.calculate_fare()
print(f"Total fare for the bus: ${total_fare}")
