def number_to_words(n: int) -> str:
    """
    Converts an integer into its English word representation.
    Example: 42 → "forty-two"

    Note: Only handle from 0 to 999,999
    """
    ones = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    hundreds = []

    if n < 20:
        return ones[n]
    elif 20 <= n < 100:
        result = divmod(n,10)
        tens_index = result[0]
        ones_index = result[1]

        if  ones_index == 0:
            return str(tens[tens_index])
        return str(tens[tens_index] + " " +  ones[ones_index])

    elif 99 < n < 1000:

        # to get hundreds
        # result = n//100

        result = n % 100
        print(ones[]result)



        # ones_index = result[1]
        # tens_index = result[0]
        #
        # print(ones_index,tens_index)
        return ""

    else:
        return "Error"




user_input = input("Enter a number: ")

converted_number  = number_to_words(int(user_input))
print(converted_number)



