# Question 1
a = 16

a = a // 2

print(a**2)

a = a + 11

print(a+1)

a = a - 3
print(a)

# Question 2
print((2+3)*6/2 and 18.0)

# Question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

# Question 4
def palindrome(word):

    if word == word[::-1]:
        return True
    else:
        return False

# Ask the user for input
word = input("Enter a word to check if it's a palindrome: ")

# Call the function with the user input and display the result
if palindrome(word):
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

# Question 5

import string

def count_un_an_words(text):
    words = text.split()  # Split the text into words
    count = 0  # Initialize counter

    for word in words:  # Iterate through words
        word = word.strip(string.punctuation).lower()  # Remove punctuation and convert to lowercase
        if word.startswith("un") and word.endswith("an"):  # Check pattern
            count += 1  # Increase counter

    return count  # Return the total matches

# Ask the user for input
text = input("Enter the text to check for 'un' and 'an' words: ")
result = count_un_an_words(text)
print(f"Number of 'un' and 'an' words: {result}")

# Question 6
# Creating a string
my_string = "hello"
print("Original string:", my_string)

# Trying to change the first letter (this will cause an error)
# my_string[0] = 'H'  # This line would cause a TypeError

# Correct way: Create a new string
new_string = "H" + my_string[1:]
print("Modified string:", new_string)

# The original string remains unchanged
print("Original string after attempted change:", my_string)

# Question 7
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# Use a loop to modify the list
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 1:  # Check if the number is odd
        random_numbers[i] = None  # Mark it for removal
    else:
        random_numbers[i] *= 2  # Double even numbers

# Remove all 'None' values (which were odd numbers)
random_numbers = [num for num in random_numbers if num is not None]

# Print the final modified list
print("Modified list:", random_numbers)

# Question 8
def is_valid_url(text):

    if text.startswith("http://"):  # Check if it starts with "http://"
        if " " in text or text.endswith("/"):  # Ends with a space or "/"
            return True
    return False


url = input("Enter a URL: ")  # Ask user for input
if is_valid_url(url):
    print("Valid URL")
else:
    print("Invalid URL")

# Question 9
def days_since_birthday(birthday):
    parts = birthday.split("-")  # Split using "-"
    birth_year = int(parts[2])  # Convert year to integer
 # Get the current year by asking the user
    current_year = int(input("Enter the current year: "))
    # Compute whole years between birth year and current year (excluding both)
    whole_years = (current_year - birth_year - 1)

    # Calculate leap years
    leap_years = 0
    for year in range(birth_year + 1, current_year):  # Iterate through the whole years
        if is_leap_year(year):
            leap_years += 1
    regular_years = whole_years - leap_years
    total_days = (regular_years * 365) + (leap_years * 366)

    return total_days
    # Each year has 365 days (ignoring leap years)
    return whole_years * 365
def is_leap_year(year):

    # Determines if a year is a leap year.

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# User imput
birthday = input("Enter your birthday (DD-MM-YYYY): ")
days = days_since_birthday(birthday)
print(f"Whole years in days since birth: {days}")






