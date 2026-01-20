"""
===============================================
Assignment [mini activity 7] 
Student Name: [conner]
Date: [sept 22nd]

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say your name!
# Write a program that displays your name!
# =======================================================

# --- Put your code here ---

# Ask for there age
age = int(input("Enter your age: "))

#Ask if they have perental permision
permission = input("Do you have perental permission? (yes/no): ").lower()

# check the age

if age >= 18:
    print("you can watch the movie")
elif age < 18 and permission == "yes":
    print("you can watch the movie")
else:
    print("you cannot watch the movie")
