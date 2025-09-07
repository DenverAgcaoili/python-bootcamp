# TODO: Fill in the details of the item you plan to buy
wishlist = [
    {
        "Name": "Phone",
        "Cost": 20_000,
        "Info": "brand",
        "Stock": 12
    },
    {
        "Name": "Keyboard",
        "Cost": 1_000,
        "Info": "Wireless",
        "Stock": 1
    },
    {
        "Name": "Jacket",
        "Cost": 2_000,
        "Info": "Waterproof",
        "Stock": 100
    },
    {
        "Name": "Cap",
        "Cost": 500,
        "Info": "Baseball",
        "Stock": 13
    }
]


# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
order = wishlist[0]
print(order)
for key,value in order.items():
    print(f"Name:\t{key}\nInfo:\t{value}")