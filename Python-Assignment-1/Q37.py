# ASSIGNMENT 1 - QUESTION 37
# Program to create a dictionary containing five countries and their capitals.

countries_capitals_dictionary = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "United Kingdom": "London",
    "France": "Paris",
    "Canada": "Ottawa"
}

print("Country and Capital Details:")
for country_name, capital_city in countries_capitals_dictionary.items():
    print("Country: " + str(country_name) + " | Capital: " + str(capital_city))
