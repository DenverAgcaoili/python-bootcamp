total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        pass  # TODO: Ask for number, add to total, and print
        number = int(input("Enter a number: "))
        total += number
        print(total)

    if command == "sub":
        pass  # TODO: Ask for number, subtract to total, and print
        number = int(input("Enter a number: "))
        total -= number
        print(total)

    elif command == "exit":
        running = False