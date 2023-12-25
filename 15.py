def compare_dictionaries(dict1, dict2):
    return dict1 == dict2

# Example usage:
dictionary1 = {'a': 1, 'b': 2, 'c': 3}
dictionary2 = {'a': 1, 'b': 2, 'c': 3}

result = compare_dictionaries(dictionary1, dictionary2)

if result:
    print("The dictionaries are equal.")
else:
    print("The dictionaries are not equal.")
