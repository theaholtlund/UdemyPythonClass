# import required libraries and modules
import pytz
import datetime

# Define a country variable
country = 'Europe/Moscow'

# Displaying time using various options
# Pytz is a third-party library that provides support for working with time zones
# It allows you to handle, manipulate and convert time zone information
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# Look at all the country names available
# for x in pytz.all_timezones:
#     print(x)
#
# Look at all the country codes available, plus the name
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# Countries can be in multiple time zones

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=': ')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
