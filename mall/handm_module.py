import time
import datetime
import random
class HMStore:
    def __init__(self):
        self.cart = []
        self.users = {}

    def display_menu(self):
        print("1. Clothing")
        print("2. Accessories")
        print("3. Makeup")

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

    def add_to_cart(self, item, price, quantity, size=None):
        self.cart.append((item, price, quantity, size))

    def display_cart(self):
        print("\nYour Shopping Cart:")
        for item, price, quantity, size in self.cart:
            print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")
        total_price_hm = sum(price * quantity for _, price, quantity, _ in self.cart)
        print(f"\nTotal Price: ${total_price_hm}")
        return total_price_hm, self.cart

    

def display_feedback():
    print("\n=========================")
    print("Feedback:")
    print("Thank you for shopping with H&M!")
    print("We value your feedback. Please leave a review.")
    feedback = input("Enter your feedback: ")
    print("Feedback submitted successfully!")
    print("=========================")

