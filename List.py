# Original list
original_list = [1, 2, 3]

# i. By using + operator
extended_list_operator = original_list + [4, 5, 6]

# ii. By using append()
extended_list_append = original_list.copy()  # Copy the original list to avoid modifying it
extended_list_append.append(4)
extended_list_append.append(5)
extended_list_append.append(6)

# iii. By using extend()
extended_list_extend = original_list.copy()  # Copy the original list to avoid modifying it
extended_list_extend.extend([4, 5, 6])

# Print the results
print("Original List:", original_list)
print("Extended List (+ operator):", extended_list_operator)
print("Extended List (append()):", extended_list_append)
print("Extended List (extend()):", extended_list_extend)
