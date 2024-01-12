def calculate_factorial(number):
    """
    Calculate the factorial of a given number using a for loop.
    """
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i
    return factorial_result

# Input value
num = int(input("Enter a number: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate and display the factorial
    result = calculate_factorial(num)
    print(f"The factorial of {num} is: {result}")
