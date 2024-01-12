def is_armstrong_number(number):
    """
    Check if the given number is an Armstrong number.
    """
    num_str = str(number)
    order = len(num_str)
    sum_of_digits = sum(int(digit) ** order for digit in num_str)
    
    return number == sum_of_digits

# Input value
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
