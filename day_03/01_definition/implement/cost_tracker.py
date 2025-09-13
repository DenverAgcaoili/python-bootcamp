class CostTracker:
    def __init__(self, items=None):
        if items:
            self.expenses = items
        else:
            self.expenses = []

    def spend(self):
        """TODO: Add a new cost in expenses"""
        item_cost = int(input("Enter item cost: "))
        item_count = int(input("Enter item count: "))
        total_item_cost = item_cost * item_count
        self.expenses.append(total_item_cost)
        return self.expenses

    def refund(self):
        """TODO: Remove the last cost added (if any)"""
        if self.expenses:
            self.expenses.pop(-1)

    def show(self):
        """TODO: Print the current list of expenses and total"""
        print(self.expenses)

    def save(self):
        """TODO: Save the current list of expenses to a new file"""
        with open("expenses.txt", "a") as file:
            for expense in self.expenses:
                print(expense)
                file.write(f"{expense}\n")

    def load(self):
        """TODO: Save the current list of expenses to a new file"""
        loaded_expenses = []
        with open("expenses.txt", "r") as file:
            file_contents = file.readlines()

            for file_content in file_contents:
                number = float(file_content.replace("\n", ""))
                print(number)
                loaded_expenses.append(number)
            return loaded_expenses

    def main_loop(self):
        running = True

        while running:
            command = input("Command: ")

            if command == "spend":
                self.spend()
            elif command == "refund":
                if not self.expenses:
                    print("Expenses is currently empty")
                self.refund()
            elif command == "show":
                self.show()
            elif command == "save":
                self.save()
            elif command == "load":
                self.expenses = self.load()

            elif command == "exit":
                running = False



expense_1 = CostTracker()
expense_1.main_loop()

