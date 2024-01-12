def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest using the formula: SI = P * R * T / 100
    where:
    P = Principal amount
    R = Rate of interest
    T = Time (in years)
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input values
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest: "))
time_period = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_period)

# Display the result
print(f"Simple Interest: {simple_interest_result}")
