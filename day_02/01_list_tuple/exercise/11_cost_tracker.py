def spend(expenses):
    """TODO: Add a new cost in expenses"""
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    expenses.append(total_item_cost)
    return expenses

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    if expenses:
         expenses.pop(-1)

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)

def save(expenses):
    """TODO: Save the current list of expenses to a new file"""
    with open("expenses.txt","a") as file:
        for expense in expenses:
            file.write(f"{expense}\n")

def load():
    """TODO: Save the current list of expenses to a new file"""
    loaded_expenses = []
    with open("expenses.txt","r") as file:
        file_contents = file.readlines()

        for file_content in file_contents:
            number = float(file_content.replace("\n",""))
            loaded_expenses.append(number)
        return loaded_expenses


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")

        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            if not current_expenses:
                print("Expenses is currently empty")
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "save":
            save(current_expenses)
        elif command == "load":
            loaded_expense = load()
            current_expenses.extend(loaded_expense)

        elif command == "exit":
            running = False


main()
