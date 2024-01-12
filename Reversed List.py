# Define a sample list
original_list = [1, 2, 3, 4, 5]

# Method 1: Using the reverse method
reversed_list_method1 = original_list.copy()  # Create a copy to keep the original list unchanged
reversed_list_method1.reverse()

# Method 2: Using slicing
reversed_list_method2 = original_list[::-1]

# Display the original and reversed lists
print("Original List:", original_list)
print("Reversed List (Method 1 - using reverse method):", reversed_list_method1)
print("Reversed List (Method 2 - using slicing):", reversed_list_method2)
