def parse_email(email):
    """
    Parse the email address and return a tuple of username and domain.
    """
    # Split the email address into username and domain
    username, domain = email.split('@', 1)

    # Return a tuple of username and domain
    return username, domain

# Input value
email_address = input("Enter an email address: ")

# Parse the email address and form a tuple
result_tuple = parse_email(email_address)

# Display the result
print("Username:", result_tuple[0])
print("Domain:", result_tuple[1])
