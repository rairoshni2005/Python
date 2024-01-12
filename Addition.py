class InputNumbers:
    def __init__(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

class AddNumbers(InputNumbers):
    def __init__(self):
        # Call the constructor of the base class to get user input
        super().__init__()

    def add_and_display(self):
        result = self.num1 + self.num2
        print(f"The sum of {self.num1} and {self.num2} is: {result}")

# Example usage:
addition_object = AddNumbers()
addition_object.add_and_display()
