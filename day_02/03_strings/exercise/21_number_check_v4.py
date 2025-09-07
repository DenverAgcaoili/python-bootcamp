# Ask the user for an input
user_input = input("Enter number: ").strip()

# TODO: Remove extra spaces
inputs = user_input.split()
new_input = "".join(inputs)
print(new_input)

# TODO: Remove commas
new_input = new_input.replace(",","")
print(new_input)

# TODO: Remove extra spaces
new_input = new_input.replace(" ","")
print(new_input)

# TODO: If user enters a valid number
new_input=int(new_input)
print(new_input + 1)

# TODO: Else
# print("Please enter a valid number!")
