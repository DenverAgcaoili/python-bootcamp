prices = [10_000, 20, 3_000, 3, 2, 1_000]

# TODO: Change the first, third, and last values to half the price

# Show the changed list
indices =[0,2,-1]
for index in indices:
    discounted_prices = prices[index]/2
    print (f"Discounted price is: {discounted_prices}")

