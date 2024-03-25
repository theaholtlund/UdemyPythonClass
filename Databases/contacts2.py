# Importing SQLite to Python
import sqlite3

# Create the database if it does not already exist
db = sqlite3.connect("contacts.sqlite")

# Using the cursor to update the database
# Because we have used a cursor, we cna use the rowcount property to see how many rows were updated
new_email = "newemail@update.com"
phone = 4567890
update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print(f"{update_cursor.rowcount} rows were updated")

# Confirming that the connection for the db is the same as the one for the cursor
print(f"Are the connections the same: {update_cursor.connection == db}")

# Committing the changes to the database
update_cursor.connection.commit()
update_cursor.close()

# Iterating over rows
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()
