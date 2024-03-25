# Importing SQLite to Python
import sqlite3

# Create the database if it does not already exist
# If it does, then the code will open it
# Create tables in the database, if they do not already exist
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Thea', 12345678, 'thea@hotmail.com')")
db.execute("INSERT INTO contacts VALUES('Tim', 4567890, 'tim@hotmail.com')")

# Access cursor to query and manipulate database
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
print(cursor.fetchall()) # Returns a list containing a tuple for each row in the database
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# Close off the cursor and database connection after executing
cursor.close()
db.commit() # Committing the changes before closing the database
db.close()
