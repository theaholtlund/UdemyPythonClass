# Import JSON module
import json
import urllib.request

# Define what file we want to work with and bind it to a variable
json_data_source_file = 'temperature_anomaly.json'
json_data_source_url = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

# Open the file in text mode, for reading, as this is the default mode
# with open(json_data_source_file, encoding='utf-8') as data:
#     anomalies = json.load(data)

# Open the file from the URL for the data
with urllib.request.urlopen(json_data_source_url) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

# Print the description in the JSON file
    print(anomalies['description'])

# Iterate over the years in the data file
for year, value in anomalies['data'].items():
    year, value = int(year), float(value) # Convert string values to ints and floats
    print(f"{year} ... {value:6.2f}") # Print values in a field width of 6 chars, aligned to the right

# Print the citation in the JSON file
print(anomalies['citation'])
