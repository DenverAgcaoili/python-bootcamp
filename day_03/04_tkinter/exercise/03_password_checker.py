import tkinter

root = tkinter.Tk()


# TODO: Add label for instructions
instruction_label = tkinter.StringVar(root, value="Enter your password:")
label = tkinter.Label(root, textvariable=instruction_label)
label.pack()

# TODO: Add entry for instructions
password_entry = tkinter.Entry(root,show="*")
password_entry.pack()

# TODO: Add StringVar for instruction
instruction_update = tkinter.StringVar(root, value="Enter your password and press enter")

# TODO: Add label using StringVar
label_update = tkinter.Label(root, textvariable=instruction_update)
label_update.pack()

def check_password(event=None):
    correct_password = "pass"
    given_text = password_entry.get()
    if given_text ==correct_password:
        instruction_update.set("Password Correct! Access granted.")
    else:
        instruction_update.set("Incorrect password! Try again.")

    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password
root.bind("<Return>",check_password)
button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()
root.mainloop()
