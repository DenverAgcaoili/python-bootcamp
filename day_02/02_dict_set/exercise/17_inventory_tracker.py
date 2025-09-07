def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)

def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""
    print(type(inventory))
    print(inventory[index])
    # return inventory[index]


def show(inventory):
    """TODO: Print the items and their details line-by-line"""
    print("Inventory: ")
    for index,order in enumerate(inventory,start=0) :
        print(f"Order number {index}")
        for key,value in order.items():
             print(f"\t{key}:{value}")




def main():
    running = True
    inventory = [
    {
        "Name": "Phone",
        "Cost": 20_000,
        "Info": "brand",
        "Stock": 12
    },
    {
        "Name": "Keyboard",
        "Cost": 1_000,
        "Info": "Wireless",
        "Stock": 1
    },
    {
        "Name": "Jacket",
        "Cost": 2_000,
        "Info": "Waterproof",
        "Stock": 100
    },
    {
        "Name": "Cap",
        "Cost": 500,
        "Info": "Baseball",
        "Stock": 13
    }
]


    while running:
        command = input("Command: ")

        if command == "add":
            # TODO: Use add command"""
            name = input("Enter Name: ")
            cost = input("Enter Cost: ")
            info = input("Enter Info: ")
            stock = input("Enter Stock: ")

            item = {
                "Name": name,
                "Cost": cost,
                "Info": info,
                "Stock": stock
            }
            add(inventory, item)
            print(inventory)

        elif command == "remove":
            #  TODO: Use remove command"""
            index = int(input("Enter item index to remove: "))
            remove(inventory, index)
            pass
        elif command == "read":
            # TODO: Use read command"""
            index = int(input("Enter order index to read: "))
            read(inventory, index)
            pass
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
            pass
        elif command == "exit":
            running = False


main()
