# Importing the data from the country_info.py file, storing it in a variable
# This is good practice, to reduce the risk of error if using the same file repeatedly
input_filename = 'country_info.txt'

# Define an empty dictionary to let the user choose a country by the country name
countries = {}

# If no mode parameter is passed ti the open() function, "r" will be the default
# Unpacking the variables for each row, as there are seven variables in each row
# If our list had fewer than seven items, the code would crash
with open(input_filename) as country_file:
    country_file.readline() # This code discards the headings, as the code then moved on to the next item
    for row in country_file:
        data = row.rstrip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep="\n\t")
        # Creating a dictionary with the values unpacked from the line of text
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        # Add each entry to the countries dictionary inside the loop
        countries[country.casefold()] = country_dict
        # Allow a user to use the country code to look up the country
        # As dictionaries can have more than one key, we can add the country code as a key
        # Each dictionary country will then have two references, one with country name key and one with country code key
        # However, note that the individual country dictionaries are not duplicated
        countries[code.casefold()] = country_dict

# Print the dictionary, where each key is the name of the country and the values are the dictionaries for that country
# This will be a dictionary containing dictionaries
print(countries)

# Get a country from the user, and then display the capital city for that chosen country
while True:
    chosen_country = input("Please choose a country to see the capital: ").casefold()
    if chosen_country in countries:
        country_data = countries[chosen_country]
        capital = country_data['capital']
        print(f"The capital for {chosen_country.capitalize()} is {capital.capitalize()}")
    elif chosen_country == "quit":
        break
    else:
        print("Please type in a valid country")
