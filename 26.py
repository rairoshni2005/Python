class Store:
    def __init__(self):
        # Dictionary to store product codes and their prices
        self.product_catalog = {
            'P001': 10.0,
            'P002': 15.0,
            'P003': 20.0,
            'P004': 25.0,
            'P005': 30.0,
        }

    def display_menu(self):
        print("Product Menu:")
        for code, price in self.product_catalog.items():
            print(f"{code}: ${price}")

    def generate_bill(self, quantities):
        total_amount = 0.0

        print("\nBill:")
        for code, quantity in quantities.items():
            if code in self.product_catalog:
                price = self.product_catalog[code]
                total_price = price * quantity
                total_amount += total_price
                print(f"Product {code}: ${price} x {quantity} = ${total_price}")

        print("\nTotal Amount: ${:.2f}".format(total_amount))


# Example usage:
def main():
    store = Store()

    # Display the product menu
    store.display_menu()

    # Prompt user to enter quantity for each product
    quantities = {}
    for code in store.product_catalog.keys():
        quantity = int(input(f"Enter quantity for product {code}: "))
        quantities[code] = quantity

    # Generate and display the bill
    store.generate_bill(quantities)


if __name__ == "__main__":
    main()
