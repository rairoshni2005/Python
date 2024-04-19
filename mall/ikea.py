class Furniture:
    def __init__(self, name, material, color, quantity, usage, price):
        self.name = name
        self.material = material
        self.color = color
        self.quantity = quantity
        self.usage = usage
        self.price = price

    def display_details(self):
        print(f"\n{self.name} Details:")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")
        print(f"Quantity: {self.quantity}")
        print(f"Usage: {self.usage}")
        print(f"Price: ₹{self.price * self.quantity}")


class Chair(Furniture):
    def __init__(self, material, color, quantity, usage, has_armrest=False):
        super().__init__("Chair", material, color, quantity, usage, price=50)  # Assuming $50 per chair
        self.has_armrest = has_armrest

    def display_details(self):
        super().display_details()
        print(f"Has Armrest: {self.has_armrest}")


class Table(Furniture):
    def __init__(self, material, color, quantity, usage, shape="Rectangle"):
        super().__init__("Table", material, color, quantity, usage, price=100)  # Assuming $100 per table
        self.shape = shape

    def display_details(self):
        super().display_details()
        print(f"Shape: {self.shape}")


class Sofa(Furniture):
    def __init__(self, material, color, quantity, usage, has_sleeper=False):
        super().__init__("Sofa", material, color, quantity, usage, price=200)  # Assuming $200 per sofa
        self.has_sleeper = has_sleeper

    def display_details(self):
        super().display_details()
        print(f"Has Sleeper: {self.has_sleeper}")


class Bed(Furniture):
    def __init__(self, material, color, quantity, usage, size="Single"):
        super().__init__("Bed", material, color, quantity, usage, price=150)  # Assuming $150 per bed
        self.size = size

    def display_details(self):
        super().display_details()
        print(f"Size: {self.size}")


def generate_bill(cart):
    total_cost_ikea = 0
    exchange_rate = 75  # Assuming an exchange rate of 75 rupees per dollar
    print("\n\n---------------------- Bill ----------------------")
    for item in cart:
        item.display_details()
        total_cost_ikea += item.price * item.quantity
        print("---------------------------------------------------")
    total_cost_in_rupees = total_cost_ikea * exchange_rate
    print(f"Total Cost: ₹{total_cost_in_rupees}")
    print("---------------------------------------------------")


