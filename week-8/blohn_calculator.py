#==============================================================================
# Title: blohn_calculator.py
# Author: Janet Blohn
# Date:   06/17/2020
# Modified Date: n/a
# Description: Exercise 8.3 Mathematical Functions
# Date formatted from: https://phoenixnap.com/kb/get-current-date-time-python
# and https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
#==============================================================================

first_name = "Janet"
last_name = "Blohn"
exercise = "Exercise 8.3"
from datetime import date
today=date.today()

print(first_name + " " + last_name)
print(exercise)
print(today.strftime("%B %d, %Y"))
print()

def add(number1, number2):
  return number1 + number2

def subtract(number1, number2):
  return number1 - number2

def divide(number1, number2):
  return number1 / number2

print(add(10, 30))
print(subtract(60, 40))
print(divide(100, 25))
