def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input value
num = int(input("Enter a number: "))

# Check if the number is even or odd
result = check_even_odd(num)

# Display the result
print(f"The number {num} is {result}.")
