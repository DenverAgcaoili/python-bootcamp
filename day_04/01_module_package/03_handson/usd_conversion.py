import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")

# Get the latest conversion rate from USD to PHP

conversion = response.json()
rates = conversion['rates']

print(f"Conversion rate of PHP to USD: {rates['PHP']}")

