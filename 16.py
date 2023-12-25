def create_odd_cubes_dictionary(start, end):
    odd_cubes_dict = {}

    for number in range(start, end + 1):
        if number % 2 != 0:
            odd_cubes_dict[number] = number ** 3

    return odd_cubes_dict

# Example usage:
start_range = 1
end_range = 10

result_dictionary = create_odd_cubes_dictionary(start_range, end_range)

print("Dictionary of cubes of odd numbers in the range {}: {}".format((start_range, end_range), result_dictionary))
