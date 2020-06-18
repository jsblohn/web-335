#==============================================================================
# Title: blohn_hello_world.py
# Author: Janet Blohn
# Date:   06/17/2020
# Modified Date: n/a
# Description: Exercise 8.2 - Hello World Demo
# Date formatted from: https://phoenixnap.com/kb/get-current-date-time-python
# and https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#==============================================================================

# Create Variables for Heading
first_name = "Janet"
last_name = "Blohn"
exercise = "Exercise 8.2"
from datetime import date
today=date.today()

#Print Heading and "Hello World"
print(first_name + " " + last_name)
print(exercise)
print(today.strftime("%B %d, %Y"))
print()
print("Hello World")
