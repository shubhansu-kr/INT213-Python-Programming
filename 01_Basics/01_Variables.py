# There is more than one way to do it 

# Data types in python

# Numbers
# Strings
# Boolean

""" 
Convetions in python programming

1. variable name -> smallercase 
2. constants name -> uppercase

Types of case : 

1. snake_case
2. camelCase 

No special symbol in the var name 
> same as c++ 


"""

courseCode = 'Int213'
print(courseCode)

expression = 4+3/2
print(expression)

#  When we use division the default data type is float
# Float Division '/'
div = 4/2
print(div)

# Interger Division '//'

div = 4 // 2
print (div)

# Strings - single quote or double quote -> same 
name = 'john'
print(name)

name = "bob"
print(name)

# string does not hold any meaning, its just a collection of char
greeting = 'hello'

print (greeting, 'Welcome to Python lecture')

# Marks 

studentName = 'Atut'
section = 'K21GP'

mathsMarks = 78
englishMarks = 94
scienceMarks = 85

marksPercentage = (mathsMarks + englishMarks + scienceMarks)/3

print (
    'Name: ', studentName, '\n'
    'Section: ', section, '\n'
    'Maths: ', mathsMarks, '\n'
    'English: ', englishMarks, '\n'
    'Science: ', scienceMarks, '\n'
    'Percentage: ', marksPercentage, '\n'
)

name = 'cherry' 

greeting = 'Hello, ' + name + '! How are you?'
print (greeting)

age = 10

# var = 'You are ' + age   --> Error since we cannot add a num to string

# str() function used to convert number into string
age_str = str(age)

var = 'You are ' + age_str
print (var)

print(type(age))
print(type(age_str))

name = 7
welcome = 'See you at {}'

# WE can also achieve concatination with string formatting 
# f is used to denote the use of fstream, placed before string
if (age < 18): var = f'Your age is {age}, You cannot come to the party'
else : var = welcome.format(name)

print (var)