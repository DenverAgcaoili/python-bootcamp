# Price notification template
price_notification = "The price of {order} is ${amount}."

# TODO: Post: Latte ($3.5)
formatted_price_notification = price_notification.format(order=input("Enter order 1: "),amount="3.5")
print(formatted_price_notification)

# TODO: Post: Espresso ($2.75)
formatted_price_notification = price_notification.format(order="Espresso",amount="2.75")
print(formatted_price_notification)

# TODO: Post: Cappuccino ($4.0)
formatted_price_notification = price_notification.format(order="Cappuccino",amount="4.0")
print(formatted_price_notification)