def check_vowel(character):
    """
    Check if the given character is a vowel.
    """
    vowels = "aeiouAEIOU"
    if character in vowels:
        return True
    else:
        return False

# Input value
char = input("Enter a character: ")

# Check if the character is a vowel
if len(char) == 1 and char.isalpha():
    if check_vowel(char):
        print(f"The character {char} is a vowel.")
    else:
        print(f"The character {char} is not a vowel.")
else:
    print("Please enter a single alphabetical character.")
