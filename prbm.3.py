class ShoppingCart:
    def __init__(self):
        # Initialize an empty dictionary to represent the items in the cart
        self.cart_items = {}

    def add_item(self, item_name, price, quantity=1):
        # Add an item to the cart or update its quantity if already present
        if item_name in self.cart_items:
            self.cart_items[item_name]['quantity'] += quantity
        else:
            self.cart_items[item_name] = {'price': price, 'quantity': quantity}
        print(f"Added {quantity} {item_name}(s) to the cart.")

    def remove_item(self, item_name, quantity=1):
        # Remove an item from the cart or update its quantity
        if item_name in self.cart_items:
            current_quantity = self.cart_items[item_name]['quantity']
            if quantity >= current_quantity:
                del self.cart_items[item_name]
            else:
                self.cart_items[item_name]['quantity'] -= quantity
            print(f"Removed {quantity} {item_name}(s) from the cart.")
        else:
            print(f"{item_name} not found in the cart.")

    def calculate_total_price(self):
        total_price = 0
        for item_name, item_info in self.cart_items.items():
            total_price += item_info['price'] * item_info['quantity']
        return total_price

    def display_cart(self):
        print("Shopping Cart:")
        for item_name, item_info in self.cart_items.items():
            print(f"{item_name}: ${item_info['price']} x {item_info['quantity']}")

# Example usage:
cart = ShoppingCart()

cart.add_item(item_name="Laptop", price=800, quantity=2)
cart.add_item(item_name="Headphones", price=50)
cart.add_item(item_name="Mouse", price=20)

cart.display_cart()
print("Total Price: ${:.2f}".format(cart.calculate_total_price()))

cart.remove_item(item_name="Laptop", quantity=1)

cart.display_cart()
print("Total Price after Removal: ${:.2f}".format(cart.calculate_total_price()))
