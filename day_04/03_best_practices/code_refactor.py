def add_grade():
    pass
    subject = input("Subject: ")
    score = float(input("Score: "))
    grades.append({"subject": subject, "score": score})
    print("Grade added!")


def view_average():
    pass
    if grades:
        total = sum(g["score"] for g in grades) / len(grades)
        print("Grades:")
        for g in grades:
            print(f"- {g['subject']}: {g['score']}")
        print(f"Average = {total:.2f}")
    else:
        print("No grades yet.")


def exit_program() -> bool:
    print("Thanks")
    return False


def main():
    grades = []
    running = True

    while running:
        print("\n1. Add Grade\n2. View Average\n3. Exit")

        choice = input("Choose: ")
        valid_choices =["1","2","3"]


        if not choice in valid_choices:
            print("Invalid choice.")

        elif choice == "1":
            add_grade()

        elif choice == "2":
            view_average()

        elif choice == "3":
            running = exit_program()

main()