def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total + total_item_cost


def sub(total):
    """TODO: Remove total item cost (cost, count) from total and return"""
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total - total_item_cost

def show(total):
    """TODO: Print total"""
    print(f"Your balance is {total}")

def main():
    total = 0
    running = True
    while running:
        command = input("Provide command[add/sub/show/exit]: ")
        if command == "add":
            total = add(total)

        elif command == "sub":
            total = sub(total)

        elif command == "show":
            show(total)

        elif command == "exit":
            print("Thankyou!")
            running = False
        else:
            print("Invalid command!")
            running = False
main()
