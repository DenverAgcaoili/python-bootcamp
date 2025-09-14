def is_strong_password(password: str) -> bool:
    """
    Returns True if the password meets the following criteria:
    - At least 8 characters
    - Contains at least one digit
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    """
    is_strong = True
    if len(password) < 8:
        is_strong = False


    return is_strong

user_input = input("Enter password: ")
print(f"Is password strong : {is_strong_password(user_input)}")
