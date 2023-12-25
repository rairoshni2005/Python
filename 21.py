def is_perfect_number(number):
    if number <= 0:
        return False  # Perfect numbers are positive integers

    # Find divisors and sum them
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    # Check if the sum of divisors equals the original number
    return divisor_sum == number

# Example usage:
num_to_check = 28

if is_perfect_number(num_to_check):
    print(f"{num_to_check} is a perfect number.")
else:
    print(f"{num_to_check} is not a perfect number.")
