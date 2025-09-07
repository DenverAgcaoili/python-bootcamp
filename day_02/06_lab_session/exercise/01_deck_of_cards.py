def create_deck() -> list[str]:
    """TODO: Return a list of 52 strings containing a standard deck"""
    # deck = [0] * 52
    deck = []
    ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")

    for suit in suits:
        for rank in ranks:
            pass
            deck.append(str(rank) + " of " + str(suit))
    # print(deck)
    return list(deck)


def draw_top(deck: list[str], count: int=1)-> list[str]:
    """TODO: Remove count return count cards from the start from deck"""


def draw_bottom(deck: list[str], count: int=1) -> list[str]:
    """TODO: Remove and return count cards from the end of the deck"""

def draw_random(deck: list[str], count: int=1) -> list[str]:
    """TODO: Remove and return count random cards from the deck"""

def show(deck):
    """TODO: Print all cards in deck"""
    print(deck)

def add_top(deck: list[str], other: list[str]):
    """TODO: Add cards in other to the first parts of deck"""

def add_bottom(deck: list[str], other: list[str]):
    """TODO: Add cards in other to the last parts of deck"""

def add_random(deck: list[str], other: list[str]):
    """Challenge: TODO: Add cards in other randomly to deck"""

def load(filename: str) -> list[str]:
    """Challenge: TODO: Returns a list of cards loaded from a file"""

def save(deck: list[str], filename: str):
    """Challenge: TODO: Saves a list of cards into a file (retrievable with load)"""

def main():
    commands = {
        "create": create_deck,
        "draw top": draw_top,
        "draw bottom": draw_bottom,
        "draw random": draw_random,
        "show": show,
        "add top": add_top,
        "add bottom": add_bottom,
        "add random": add_random,
        "load": load,
        "save": save
    }
    # print(commands)

    user_command = input("Enter a command: ").lower().strip()
    deck =[]
    if user_command not in commands:
        print("Invalid command!")
    elif user_command == "create":
        new_deck = commands[user_command]()
        deck.clear()
        deck.append(new_deck)
    elif user_command == "show":
        commands[user_command](deck)

        pass







main()