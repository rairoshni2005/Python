def create_tuples_with_cubes(input_list):
    """
    Create a list of tuples from the given list, adding the cube of each number to the tuple.
    """
    result_list = [(num, num ** 3) for num in input_list]
    return result_list

# Input list
c = [2, 3, 4, 5, 6, 7, 8, 9]

# Create a list of tuples with cubes
result_tuples = create_tuples_with_cubes(c)

# Display the result
print("List of tuples with number and its cube:")
for item in result_tuples:
    print(item)
