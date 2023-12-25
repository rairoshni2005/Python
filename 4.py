def print_first_n_natural_numbers_and_sum(n):
    """
    Print the first n natural numbers and their sum.
    """
    sum_of_numbers = 0

    print(f"First {n} natural numbers:")
    for i in range(1, n + 1):
        print(i, end=" ")
        sum_of_numbers += i

    print(f"\nSum of the first {n} natural numbers: {sum_of_numbers}")

# Input value
n = int(input("Enter the value of n: "))

# Print first n natural numbers and their sum
print_first_n_natural_numbers_and_sum(n)

