class Vehicle:
    # Class attribute with a default value of 'white'
    color = 'white'

    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        # Default fare calculation: seating capacity * 100
        return self.capacity * 100

# Example usage:
vehicle_instance = Vehicle(capacity=4)

# Accessing the class attribute 'color'
print(f"Vehicle color: {Vehicle.color}")

# Accessing the class attribute 'color' through an instance
print(f"Vehicle instance color: {vehicle_instance.color}")
