# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "JP": "Japan",
    "KR": "Korea"
}

# TODO: Print the country for the given country code
country_code = input("Enter country code: ")
print(country_codes.get(country_code))

# TODO: # If the key is not found, print Unknown


# TODO: Print all codes
for country in country_codes.keys():
    print(country)

# TODO: Print all countries
for country in country_codes.values():
    print(country)