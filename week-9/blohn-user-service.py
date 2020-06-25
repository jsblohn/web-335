#==============================================================================
# Title: blohn-user-service.py
# Author: Janet Blohn
# Date:   06/24/2020
# Modified Date: n/a
# Description: Exercise 9.2 Querying and Creating Documents
# Date formatted from: https://phoenixnap.com/kb/get-current-date-time-python
# and https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#==============================================================================

# Create Variables for Heading
first_name = "Janet"
last_name = "Blohn"
exercise = "Exercise 9.2"
from datetime import date
today=date.today()

# Print Heading
print(first_name + " " + last_name)
print(exercise)
print(today.strftime("%B %d, %Y"))
print()

# Import Required Modules
from pymongo import MongoClient
import pprint
import datetime

# Define the client as the local MongoDB
client = MongoClient("localhost", 27017)

# Point to the Web335 Database
db = client.web335

# Define a new user.
user = {
  "first_name": "Andy",
  "last_name": "Griffith",
  "email": "agriffith@email.com",
  "employee_id": "020406081",
  "date_created": datetime.datetime.utcnow()
}

# Insert the new user.
user_id = db.users.insert_one(user).inserted_id

# Output the auto-generated user_id.
print(user_id)

employee_id = "020406081"

# Find and print the specified document.
pprint.pprint(db.users.find_one({"employee_id": employee_id}))
