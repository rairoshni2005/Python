def get_user_details(*args, **kwargs):
    """
    Function to take user details as input.
    
    Args:
    *args: Positional arguments for name, email, and age.
    **kwargs: Keyword arguments for additional details.

    Returns:
    Dictionary containing user details.
    """
    user_details = {}

    # Get details from positional arguments
    if len(args) >= 3:
        user_details['name'] = args[0]
        user_details['email'] = args[1]
        user_details['age'] = args[2]

    # Get additional details from keyword arguments
    user_details.update(kwargs)

    return user_details

# Example usage:
name_input = input("Enter your name: ")
email_input = input("Enter your email: ")
age_input = int(input("Enter your age: "))

additional_info = {
    'city': input("Enter your city: "),
    'phone': input("Enter your phone number: ")
}

user_data = get_user_details(name_input, email_input, age_input, **additional_info)

print("\nUser Details:")
for key, value in user_data.items():
    print(f"{key.capitalize()}: {value}")
