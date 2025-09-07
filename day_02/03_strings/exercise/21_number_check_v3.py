# Ask the user for an input
user_input = input("Enter number: ").strip()

# TODO: Remove extra spaces
# TODO: Remove commas

# TODO: If user enters a valid number
user_input = user_input.replace(",","")
print(user_input)
user_input = int(user_input)

print(user_input + 1)

# TODO: Else
print("Please enter a valid number!")
