# Import required modules and libraries
import sqlite3
import pytz

# Connecting to the database
# The detect_types parameter is used to control how the SQLite3 module interprets the data types of columns
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# Working with displaying time in different time zones
for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    local_time = pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time, local_time))


# Another alternative for how to display the time in different time zones
for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                      " history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

# Closing out the database connection
db.close()


# Closing out the database connection
db.close()
