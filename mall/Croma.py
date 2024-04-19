import time
import datetime
import random

class Electronics_:
    def __init__(self, name, menu, special_offers=None):
        self.name = name
        self.menu = menu
        self.special_offers = special_offers or {}
        self.user = None

    def welcome_user(self):
        current_time = datetime.datetime.now().time()
        greeting = "\033[92mGood morning\033[0m"
        if current_time >= datetime.time(12, 0) and current_time < datetime.time(17, 0):
            greeting = "\033[93mGood afternoon\033[0m"
        elif current_time >= datetime.time(17, 0):
            greeting = "\033[91mGood evening\033[0m"

        print(f"{greeting}, {self.user['name']}! Welcome to {self.name}.")

    def display_menu(self):
        print(f"\n{self.name} Products:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        
        if self.special_offers:
            print("\nSpecial Offers:")
            for offer, discount in self.special_offers.items():
                print(f"{offer}: {discount}% off")

    def take_order(self):
        order = {}
        while True:
            item = input("Enter the Product you want to order (or type 'done' to finish): ")
            if item.lower() == 'done':
                break
            elif item in self.menu:
                quantity = int(input(f"How many {item}s do you want? "))
                order[item] = quantity
            else:
                print("Invalid item. Please choose from the menu.")
        return order

    def calculate_total(self, order):
        total_bill_croma = sum(self.menu[item] * quantity for item, quantity in order.items())
        return total_bill_croma

    def generate_bill(self, order, total_bill_croma):
        print("\nCalculating your bill...", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)
        print("\n\033[94mOrder Summary:\033[0m")
        for item, quantity in order.items():
            print(f"{item}: {quantity} x ₹{self.menu[item]} = ₹{quantity * self.menu[item]}")
        print(f"\033[94mTotal: ₹{total_bill_croma}\033[0m")
        print("\033[92mThank you for ordering with us!\033[0m")

    def feedback(self):
        feedback_responses = [
            "Thank you for your feedback! You rated us {rating} stars.",
            "We appreciate your input! Your rating: {rating} stars.",
            "Your feedback is important to us. You gave us {rating} stars. Thank you!",
        ]

        rating = input("Please rate your experience (1 to 5 stars): ")
        if rating.isdigit() and 1 <= int(rating) <= 5:
            response = random.choice(feedback_responses).format(rating=rating)
            print(response)
        else:
            print("Invalid rating. Feedback not submitted.")
