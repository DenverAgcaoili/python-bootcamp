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