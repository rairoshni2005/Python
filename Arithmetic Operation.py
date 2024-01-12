def perform_arithmetic_operations(a, b):
    # Arithmetic Operations
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    modulus = a % b
    exponentiation = a ** b

    # Relational Operations
    equal_to = a == b
    not_equal_to = a != b
    greater_than = a > b
    less_than = a < b
    greater_than_or_equal_to = a >= b
    less_than_or_equal_to = a <= b

    # Display results
    print(f"Arithmetic Operations:")
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")
    print(f"Modulus: {modulus}")
    print(f"Exponentiation: {exponentiation}")

    print("\nRelational Operations:")
    print(f"Equal to: {equal_to}")
    print(f"Not equal to: {not_equal_to}")
    print(f"Greater than: {greater_than}")
    print(f"Less than: {less_than}")
    print(f"Greater than or equal to: {greater_than_or_equal_to}")
    print(f"Less than or equal to: {less_than_or_equal_to}")

# Input values
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

# Perform operations
perform_arithmetic_operations(operand1, operand2)
