def count_upper_lower(string_input):
    upper_count = 0
    lower_count = 0

    for char in string_input:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
string_test = 'Today is My Best Day'
upper_count, lower_count = count_upper_lower(string_test)

print("Original String:", string_test)
print("Number of Upper-case Letters:", upper_count)
print("Number of Lower-case Letters:", lower_count)
