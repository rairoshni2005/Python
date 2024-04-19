import datetime
import time
import random
from Mall_Package import AllenSolly
from Mall_Package import handm_module
from Mall_Package import kfc_bk_outlet
from Mall_Package import ikea
from Mall_Package import Croma

print("===========================================================================================")
print("|                                 WELCOME TO THE MALL                                     |")
print("|                  Enriching your shopping experience to the finest                       |")    
print("===========================================================================================")


print("We also have a limited period LOTTERY OFFER!!!! Grab it now!!!!")
print("This is a self-checkout mall so please REGISTER/LOGIN into the system to make your experience better")

class Mall:
    def __init__(self, name, stores=None):
        self.name = name
        self.stores = stores or {}
        self.user = None
        self.total_bill = 0 

    def create_account(self):
        print("\nCreate Your Account:")
        name = input("Enter your name: ")
        print()
        print()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print()
        print()
        return {"name": name, "username": username, "password": password}
        print()
        print()

    def login(self, username, password):
        if self.user and self.user["username"] == username and self.user["password"] == password:
            print()
            print("Login successful!")
            print()
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False
    def welcome_user(self):
        current_time = datetime.datetime.now().time()
        print()
        greeting = "Good morning"
        if datetime.time(12, 0) <= current_time < datetime.time(17, 0):
            greeting = "Good afternoon"
        elif current_time >= datetime.time(17, 0):
            greeting = "Good evening"
        print(f"{greeting}, {self.user['name']}! Welcome to {self.name}.")

mall = Mall("Mall")

user_account = mall.create_account()
mall.user = user_account

while True:
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    if mall.login(username_input, password_input):
        break

mall.welcome_user()
opt="Y"
while opt=="Y":
    print('--------------------------------------------------------------------------------------------')
    print('                         So, What would you like to shop today?                             ')
    print('--------------------------------------------------------------------------------------------')

    from collections import namedtuple

    MenuEntry = namedtuple('MenuEntry', ['index', 'description', 'price'])
    _menu = [
        MenuEntry(1, 'Clothing    ', 'H&M and Zara at your service!'),
        MenuEntry(2, 'Electronics ', 'Enhance electro-care for you by Croma and Vijay Sales!'),
        MenuEntry(3, 'Furniture   ', 'Comfort at your doorstep with IKEA and Pepperfry!'),
        MenuEntry(4, 'Food Outlet ', 'Give your cravings a treat with KFC and Burger King!')
    ]

    for entry in _menu:
        index = str(getattr(entry, 'index')).ljust(5)
        descr = getattr(entry, 'description').ljust(25)
        price = getattr(entry, 'price').ljust(7)
        print('{0}{1}{2}'.format(index, descr, price))

    choice = int(input("Enter Choice: "))

    if choice == 1:
        cloth_shop_choice = int(input("Which shop would you like to buy from?\n 1. Allen Solly\n2. H&M\n"))
        if cloth_shop_choice == 1:
            allen_dolly_store = AllenSolly.Allen_Solly_Store("Allen Solly Store")

            while True:
                allen_dolly_store.display_menu()
                category_choice = input("Select a category (1-4) or 'q' to quit: ")

                if category_choice == 'q':
                    break

                if category_choice == '1':
                    allen_dolly_store.display_clothing_menu()
                    clothing_choice = input("Select a clothing item (1-4): ")
                    size = input("Enter size (optional): ")
                    quantity = int(input("Enter quantity: "))
                    allen_dolly_store.add_to_cart("Clothing", 10, quantity, size)

                elif category_choice == '2':
                    allen_dolly_store.display_accessories_menu()
                    accessories_choice = input("Select an accessories item (1-4): ")
                    quantity = int(input("Enter quantity: "))
                    allen_dolly_store.add_to_cart("Accessories", 15, quantity)

                elif category_choice == '3':
                    allen_dolly_store.display_makeup_menu()
                    makeup_choice = input("Select a makeup item (1-4): ")
                    quantity = int(input("Enter quantity: "))
                    allen_dolly_store.add_to_cart("Makeup", 20, quantity)

                elif category_choice == '4':
                    allen_dolly_store.display_perfumes_menu()
                    perfume_choice = input("Select a perfume item (1-4): ")
                    quantity = int(input("Enter quantity: "))
                    allen_dolly_store.add_to_cart("Perfumes", 50, quantity)

            total_price_allensolly, cart = allen_dolly_store.display_cart()

            print("\n\n=========================")
            print("Detailed Bill:")
            for item, price, quantity, size in cart:
                print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")

            print(f"\nTotal Price: ${total_price_allensolly}")
            print("=========================")
            print()
            print("----------------------------------Let's Get your cart Going!------------------------------- ")
        opt = input("Do you want to continue? (y-yes/n-no): ").upper()

        if cloth_shop_choice == 2:
            h_and_m = handm_module.HMStore()

            while True:
                h_and_m.display_menu()
                category_choice = input("Select a category (1-3) or 'q' to quit: ")

                if category_choice == 'q':
                    break

                if category_choice == '1':
                    h_and_m.display_clothing_menu()
                    clothing_choice = input("Select a clothing item (1-4): ")
                    size = input("Enter size (optional): ")
                    quantity = int(input("Enter quantity: "))
                    h_and_m.add_to_cart("Clothing", 10, quantity, size)

                elif category_choice == '2':
                    h_and_m.display_accessories_menu()
                    accessories_choice = input("Select an accessories item (1-4): ")
                    quantity = int(input("Enter quantity: "))
                    h_and_m.add_to_cart("Accessories", 15, quantity)

                elif category_choice == '3':
                    h_and_m.display_makeup_menu()
                    makeup_choice = input("Select a makeup item (1-4): ")
                    quantity = int(input("Enter quantity: "))
                    h_and_m.add_to_cart("Makeup", 20, quantity)

            total_price, cart = h_and_m.display_cart()

            print("\n\n=========================")
            print("Detailed Bill:")
            for item, price, quantity, size in cart:
                print(f"{item} (Size: {size}, Quantity: {quantity}): ${price * quantity}")

            print(f"\nTotal Price: ${handm_module.total_price_hm}")
            print("=========================")
            print()
            print("----------------------------------Let's Get your cart Going!------------------------------- ")
    opt = input("Do you want to continue? (y-yes/n-no): ").upper()
            
    if choice==2:
        Laptops = {"Asus Rog gaming ": 100000, "Hp omen 16 ": 152000, "Asus ROG zephyrus": 78000, "MSI Katana ": 90000,
                        "Alienware F17👽": 300000, "RAZER Blade 15": 250000, "Acer Nitro 5": 580000,
                        "ROG Strix Gaming": 700000, "Dell G15 Gaming": 200000, "Macbook Air M2": 119000, "MAcbook pro M3 max": 250000}
    
        Smartphones = {"Oneplus 10 pro": 70000, "Iphone 14": 58000, "Oneplus 6T": 42000, "Mi mix 3": 88000,
                "Redmi note 12 pro": 30000, "GOOGLE pixel 8 pro": 98000, "Samsung S23 Ultra": 150000, "Iphone 15 plus":90000, "Huawei mate 6": 100000}

    # Example of special offers
        Lapptops_special_offers = {"Christmas Discount": 15, "Student Discount": 10}
        Smartphones_offers = {"Big billion days": 20, "Happy Hour": 15}

    # Create instances of Electronics_
        Laptops_ = Croma.Electronics_("Laptops", Laptops, Lapptops_special_offers)
        Smaptphones = Croma.Electronics_("Smaptphones", Smartphones, Smartphones_offers)

    # Create user account
    #     user_account = Laptops_.create_account()

    # # Set user account in the Electronics_ instances
    #     Laptops_.user = user_account
    #     Smaptphones.user = user_account

    # # Display the user's information
    #     print("\nUser Information:")
    #     print(f"Name: {user_account['name']}")
    #     print(f"Account Number: {user_account['acc_number']}")
    #     print(f"Username: {user_account['username']}")

    # Offer a choice for ordering
        print("\nSelect the item you want to order :")
        print("1. Laptops")
        print("2. Smartphones")

        outlet_choice = input("Enter the product you want to buy outlet: ")

        if outlet_choice == "1":
            Croma = Laptops_
        elif outlet_choice == "2":
            Croma = Smaptphones
        else:
            print("Invalid choice. Exiting.")
            break

    # Welcome user to the selected food outlet
        #Croma.welcome_user()

    # Display menu and take orders
        Croma.display_menu()
        order = Croma.take_order()

    # Introduce a fun loading animation
        time.sleep(1)
        print("\nGenerating your bill", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)

        total_bill_croma = Croma.calculate_total(order)
        Croma.generate_bill(order, total_bill_croma)
        

    # Ask for feedback
        time.sleep(1)  # Add a delay for a better user experience
        Croma.feedback()
    opt = input("Do you want to continue? (y-yes/n-no): ").upper()
    
    if choice == 3:
        print()
        print("============================ WELCOME TO IKEA ================================")

        cart = []

        while True:
            print("\n1. Chair\n2. Table\n3. Sofa\n4. Bed\n5. Checkout\n6. Exit")
            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                material = input("Enter material (Wood/Metal/Plastic): ")
                color = input("Enter color: ")
                quantity = int(input("Enter quantity: "))
                usage = input("Enter usage: ")
                armrest = input("Does it have armrest? (yes/no): ").lower() == "yes"
                chair = ikea.Chair(material, color, quantity, usage, has_armrest=armrest)
                cart.append(chair)

            elif choice == "2":
                material = input("Enter material (Wood/Metal/Plastic): ")
                color = input("Enter color: ")
                quantity = int(input("Enter quantity: "))
                usage = input("Enter usage: ")
                shape = input("Enter shape (default is Rectangle): ") or "Rectangle"
                table = ikea.Table(material, color, quantity, usage, shape=shape)
                cart.append(table)

            elif choice == "3":
                material = input("Enter material (Leather/Fabric): ")
                color = input("Enter color: ")
                quantity = int(input("Enter quantity: "))
                usage = input("Enter usage: ")
                sleeper = input("Does it have sleeper? (yes/no): ").lower() == "yes"
                sofa = ikea.Sofa(material, color, quantity, usage, has_sleeper=sleeper)
                cart.append(sofa)

            elif choice == "4":
                material = input("Enter material (Wood/Metal): ")
                color = input("Enter color: ")
                quantity = int(input("Enter quantity: "))
                usage = input("Enter usage: ")
                size = input("Enter size (default is Single): ") or "Single"
                bed = ikea.Bed(material, color, quantity, usage, size=size)
                cart.append(bed)

            elif choice == "5":
                if not cart:
                    print("Your cart is empty. Please add items.")
                else:
                    ikea.generate_bill(cart)
                    break

            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
            
            
        print("----------------------------------Let's Get your cart Going!------------------------------- ")
    opt = input("Do you want to continue? (y-yes/n-no): ").upper()
        
        
        
    if choice==4:
        burger_king_menu = {"Whopper": 220, "Cheeseburger": 199, "Fries": 69, "BK Grill Chicken": 280,
                        "BK Veggie": 150, "King Jr. Meals (For Kids)": 350, "Veg Chilli Cheese Melt": 219,
                        "Veggie Strips": 119, "Brownie Sundaes": 129, "Iced Tea": 100, "Coffee": 150}
    
        kfc_menu = {"Chicken Buckets": 400, "Burgers": 200, "Chicken Tenders": 270, "Rice Bowlz": 220,
                "Wraps": 120, "Hot Wings": 170, "Sides": 100, "Desserts": 90, "Beverages": 150}

    # Example of special offers
        burger_king_special_offers = {"Family Bundle": 15, "Student Discount": 10}
        kfc_special_offers = {"Super Saver Combo": 20, "Happy Hour": 15}

    # Create instances of FoodOutlet
        burger_king = kfc_bk_outlet.FoodOutlet("Burger King", burger_king_menu, burger_king_special_offers)
        kfc = kfc_bk_outlet.FoodOutlet("KFC", kfc_menu, kfc_special_offers)

    # Offer a choice for ordering
        print("\nSelect a food outlet to order from:")
        print("1. Burger King")
        print("2. KFC")

        outlet_choice = input("Enter the number of your chosen food outlet: ")

        if outlet_choice == "1":
            food_outlet = burger_king
        elif outlet_choice == "2":
            food_outlet = kfc
        else:
            print("Invalid choice. Exiting.")
            break

    # Welcome user to the selected food outlet
        #kfc_bk_outlet.FoodOutlet.welcome_user()

    # Display menu and take orders
        food_outlet.display_menu()
        order = food_outlet.take_order()

    # Introduce a fun loading animation
        time.sleep(1)
        print("\nGenerating your bill", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end='', flush=True)

        total = food_outlet.calculate_total(order)
        food_outlet.generate_bill(order, total)

    # Ask for feedback
        time.sleep(1)  # Add a delay for a better user experience
        food_outlet.feedback()
    opt = input("Do you want to continue? (y-yes/n-no): ").upper()
        
print("Thank you for shopping with us! Have a great day!") 