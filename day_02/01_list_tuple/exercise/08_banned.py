banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
user_input = input("Enter a word: ")

# TODO: If the word is in banned_words, say "Banned"
if user_input in banned_words:
    print("Banned")
else:
    print(user_input)