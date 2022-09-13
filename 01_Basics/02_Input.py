# How to take input from user - Using input function 
# input() 

""" 
Input is always in string - Age is not a number it's a string.

Convert string into intger using int()
or take input inside int()


"""

name = input('Enter user_name ')
print('Hell0,', name)

age = input('Enter your age ')
# Age is just a string 

print(f'You are {age * 12} months old') # prints input 12 times 

age_int = int(age)
print (f'You are {age_int * 12} months old')

# Or we can use int input while taking input only 
roll = int(input('Enter your roll '))

print (type(roll)) # integer input 

# Boolean variables : Either false or not false 

name = input ('Enter a Name ')
print (bool(name)) 

# Falsy Values in python 

# The following are falsy values in Python:

# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}

age = 20
age_above = age >= 18 

print (age_above) 
