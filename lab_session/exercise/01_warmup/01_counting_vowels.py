

def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""

    counter = 0
    for letter in string:
        if letter in ["a","e","i","o","u"]:
            counter += 1
    return counter

user_input = input("Enter a string: ")
print(f"Total number of vowels is: {count_vowels(user_input)}")
