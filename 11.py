def brics_countries():
    """
    Return a list of countries that are in BRICS.
    """
    brics_list = ["Brazil", "Russia", "India", "China", "South Africa"]
    return brics_list

# Get the list of BRICS countries
brics = brics_countries()

# Print the list of BRICS countries
print("Countries in BRICS:")
for country in brics:
    print(country)
