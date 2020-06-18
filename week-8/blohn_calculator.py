#==============================================================================
# Title: blohn_calculator.py
# Author: Janet Blohn
# Date:   06/17/2020
# Modified Date: n/a
# Description: Exercise 8.3 Mathematical Functions
# Date formatted from: https://phoenixnap.com/kb/get-current-date-time-python
# and https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#==============================================================================

# Create Variables for Heading
first_name = "Janet"
last_name = "Blohn"
exercise = "Exercise 8.3"
from datetime import date
today=date.today()

# Print Heading
print(first_name + " " + last_name)
print(exercise)
print(today.strftime("%B %d, %Y"))
print()

# Add Function (Add 2 numbers together and return the result)
def add(number1, number2):
  return number1 + number2

# Subtract Function (Subtract number2 from number1 and return the result)
def subtract(number1, number2):
  return number1 - number2

# Divide Function (Divide number1 by number2 and return the result)
def divide(number1, number2):
  return number1 / number2

# Run and print the results of the above functions
print(add(10, 30))
print(subtract(60, 40))
print(divide(100, 25))
