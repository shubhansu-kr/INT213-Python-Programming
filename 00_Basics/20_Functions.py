# Functions in Python 

# Two types of functions: 
# 1. Built in 
# 2. User defined 

# def is used to define a function 

# Syntax: 
def nameOfFunction(parameters): 
    return parameters ** 3

# No return type, no Parameter 
def greet(): 
    # Name is local to the function block
    name = input('Enter your name: ')
    print(f'Hello, {name}')

greet() # calling the function 

# No return type, with parameter 
def greet(name): 
    print(f'Hello, {name}')

greet('Avi') # invokes the function with parameter 

print(greet(5)) # Calls the function which is nearest in the upward direction

# Return type + parameter 
def greet(x): 
    return x ** 2; 

sq = greet(32) # invokes the function with return type 
print (sq)

# Return type + no parameter 

def greet(): 
    x = int(input('Enter num: '))
    return x ** 3

sq = greet()
print (sq) # invokes the function with no parameter and a return type 

print(greet(5))

# Using comples data structures as parameters 

def studentDetails(student): 
    n = student['name']
    m = student['marks']
    print(f'The student {n} scored {m} marks')

student = {'name': 'ABC', 'section': 'K21GP', 'marks': 45}

studentDetails(student)

