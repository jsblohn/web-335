#==============================================================================
# Title: blohn-user-service.py
# Author: Janet Blohn
# Date:   06/24/2020
# Modified Date: n/a
# Description: Exercise 9.3 Updating and Deleting Documents
# Date formatted from: https://phoenixnap.com/kb/get-current-date-time-python
# and https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#==============================================================================

# Create Variables for Heading
first_name = "Janet"
last_name = "Blohn"
exercise = "Exercise 9.3"
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

# Update a user.
db.users.update_one(
  {"employee_id": "020406081"},
  {
    "$set": {
      "email":"jblohn@my365.bellevue.edu"
    }
  }
)

employee_id = "020406081"

# Find the document and print specific fields.
pprint.pprint(db.users.find_one({"employee_id": employee_id},
{"_id": 0, "email": 1, "employee_id": 1, "first_name": 1, "last_name": 1}))
