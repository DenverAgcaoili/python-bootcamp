# Ask the user input for a color
color_input = input("Please enter a color: ")

# TODO: Print the following depending on the color input
# "green"   -> print "Go"
# "yellow"  -> print "Wait..."
# "red"     -> print "Stop"

# if color_input == "green":
#     print("Go")
# elif color_input == "yellow":
#     print("Wait")
# elif color_input == "red":
#     print("Stop")
# else:
#     print("Malfunction")

#Alternative syntax
match color_input:
    case "green"|"Green":
        print("Go")
    case "yellow":
        print("Wait")
    case "red":
        print("Stop")
    case _:
        print("Malfunction")