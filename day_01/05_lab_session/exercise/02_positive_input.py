class NegativeError (ValueError):
    pass

# TODO: Ask the user for an input that should be a number
# number = input("Enter number: ")

# TODO: Then try to convert this into an integer using the following:
#number_converted = int(number)

# The user could provide an invalid integer input (string)
# TODO: Handle this case

# The user could give a negative number
# TODO: Handle this case

# Challenge: TODO: Give the user infinite times to retry

negative_number = True
while negative_number:
    try:
        number = input("Enter number: ")
        number_converted = int(number)

        # The user could give a negative number
        if number_converted < 0:
            raise NegativeError()

        negative_number = False
        print("You entered:", number_converted)

    except NegativeError:
        print("Enter a non negative number!")
    except ValueError:
        print("Enter a valid number!")




