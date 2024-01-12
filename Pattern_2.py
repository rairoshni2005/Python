def print_pattern(rows):
    """
    Print a pattern of '*' as described.
    """
    for i in range(1, rows + 1):
        print('* ' * i)

# Input value
num_rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(num_rows)
