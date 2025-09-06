# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
#correct_credentials = (username_input == correct_username and password_input == correct_password) or (username_input == admin_username and password_input == admin_password)
correct_credentials = username_input == correct_username and password_input == correct_password
admin_login = username_input == admin_username and password_input == admin_password

if correct_credentials or admin_login:
    print("Access Granted")
else:
    print("Access Denied")