def reverse_string(string: str):
    """Return a reversed version of `string`"""

    # reversed_string = string[::-1]
    return string[::-1]

user_input = input("Enter a string: ")
print(f"Reversed string is: {reverse_string(user_input)}")
