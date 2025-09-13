import tkinter
from dataclasses import asdict
import json
root = tkinter.Tk()



# TODO: Create StringVar for name
# TODO: Create StringVar for name
name_frame = tkinter.Frame(root)
name_frame.pack()
name_label = tkinter.Label(name_frame, text="Name:")
name_label.pack(side="left", padx=20, pady=5)

name_entry = tkinter.Entry(name_frame)
name_entry.pack(side="right")


# TODO: Create StringVar for age
# TODO: Create StringVar for age
age_frame = tkinter.Frame(root)
age_frame.pack()
age_label = tkinter.Label(age_frame, text="Age:")
age_label.pack(side="left", padx=20, pady=5)

age_entry = tkinter.Entry(age_frame)
age_entry.pack(side="right")


# TODO: Create StringVar for theme
# TODO: Create StringVar for theme

theme_frame = tkinter.Frame(root)
theme_frame.pack()
theme_label = tkinter.Label(theme_frame, text="Preferred Theme:")
theme_label.pack(side="left")

radio_var = tkinter.StringVar(value="Light")

radio1 = tkinter.Radiobutton(
theme_frame, text="Light", variable=radio_var, value="Light")
radio1.pack(side="right")

radio2 = tkinter.Radiobutton(
theme_frame, text="Dark", variable=radio_var, value="Dark")
radio2.pack(side="right")



# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe
check_frame = tkinter.Frame(root)
check_frame.pack()
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    check_frame,
    text="Subscribe to newsletter",
    variable=check_value
)
checkbox.pack()


# TODO: Create IntVar for rating
# TODO: Create IntVar for rating
rate_frame = tkinter.Frame(root)
rate_frame.pack()
rate_us_label = tkinter.Label(rate_frame, text="Rate us")
rate_us_label.pack(side="left")

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    rate_frame,
    from_=0,
    to=5,
    orient="horizontal",
    variable=slider_value
)
slider.pack(side="right")


# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save

def save_to_json(event=None):
    given_name = name_entry.get()
    given_age = age_entry.get()
    selected_radio = radio_var.get()
    selected_check = check_value.get()
    selected_slider = slider_value.get()
    print(given_name,given_age,selected_radio,selected_check,selected_slider)

    # Create jason
    forms = {
        "Name": given_name,
        "Age": given_age,
        "Theme":selected_radio,
        "Subscribe":selected_check,
        "Rating": selected_slider
    }

    filepath = "forms.json"
    """TODO: Save the inventory (list[dict]) to a filepath"""
    with open(filepath, "w") as file:
        json.dump(forms, file)

root.bind("<Return>",save_to_json)
button = tkinter.Button(root, text="Submit", command=save_to_json)
button.pack()

root.mainloop()
