def remove_duplicates(input_list):
    # Using a set to store unique elements and then converting it back to a list
    unique_elements = list(set(input_list))
    return unique_elements

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
result_list = remove_duplicates(original_list)

print("Original List:", original_list)
print("List with Distinct Elements:", result_list)
