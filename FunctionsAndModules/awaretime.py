# Import required libraries and modules
import datetime
import pytz

# Defining some time zone variables
local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

# Defining some time zone objects to be aware time objects
aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time{}, time zone {} ".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))

# Working with timestamps
# The tuple specified indicates individual components of date and time
# In descending order, it specifies year, month, day, hour, minute, second and microsecond
gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())

# The UTC value the code above should be equal to
s = 1445733000
t = s + (60 * 60)

# Working with converting the timezone object
# USing the hardcoded value will ensure consistency when converting
gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
