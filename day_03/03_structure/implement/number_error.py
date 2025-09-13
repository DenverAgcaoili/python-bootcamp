
class NotNumeric(Exception):
    pass

class NotPositive(Exception):
    pass

class OutOfRange(Exception):
    pass

number = input("Enter positive number [1,100]: ")

# If input not a number, raise a custom error
# If input is not positive, raise a custom error
# If input is not between 1 and 100, raise a custom error

if not int(number):
    raise NotNumeric("value not numeric")
if int(number) < 0:
    raise NotPositive("value not positive")

raise OutOfRange("value is out of range")
