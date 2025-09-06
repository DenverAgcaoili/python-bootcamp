# TODO: Ask the user how many items will be calculated
input_count = int(input("Enter a number: "))
total = 0

# # TODO: Use a for loop to ask for more than one cost and count

for x in range(1,input_count + 1):
    # print("item_cost",x)
    item_cost = int(input("Enter cost: "))  # Let the user enter a number
    item_count = int(input("Enter count: "))  # Let the user enter a number
    item_total = item_cost * item_count
    total += item_total

print(f"Your total is {total}")
