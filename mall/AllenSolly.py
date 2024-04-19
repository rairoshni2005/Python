import time
import datetime
import random
class Allen_Solly_Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.cart = []
        self.users = {}

    def display_menu(self):
        print(f"Welcome to {self.store_name}!")
        print("1. Clothing")
        print("2. Accessories")
        print("3. Makeup")
        print("4. Perfumes")

    def display_clothing_menu(self):
        print("Clothing Options:")
        print("1. T-shirts - $10")
        print("2. Blouses - $20")
        print("3. Sweaters - $30")
        print("4. Hoodies - $25")
        # Add more clothing options as needed

    def display_accessories_menu(self):
        print("Accessories Options:")
        print("1. Hats - $15")
        print("2. Necklaces - $25")
        print("3. Bracelets - $18")
        print("4. Earrings - $12")
        # Add more accessories options as needed

    def display_makeup_menu(self):
        print("Makeup Options:")
        print("1. Foundation - $30")
        print("2. Lipstick - $15")
        print("3. Eyeshadow Palette - $25")
        print("4. Mascara - $12")
        # Add more makeup options as needed

    def display_perfumes_menu(self):
        print("Perfumes Options:")
        print("1. Floral Eau de Parfum - $50")
        print("2. Citrus Eau de Toilette - $40")
        print("3. Woody Eau de Cologne - $45")
        print("4. Oriental Eau de Parfum - $55")
        # Add more perfume options as needed

    def add_to_cart(self, item, price, quantity, size=None):
        self.cart.append((item, price, quantity, size))

    def display_cart(self):
        print("\nYour Shopping Cart:")
        for item, price, quantity, size in self.cart:
            print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")
        total_price_allensolly = sum(price * quantity for _, price, quantity, _ in self.cart)
        print(f"\nTotal Price: ${total_price_allensolly}")
        return total_price_allensolly, self.cart

   