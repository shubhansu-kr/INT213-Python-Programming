# Conditonal Statements

# Syntax 
# if (condition): 
#     (Block statement)

if 1:
    print('It\'s True')
else:
    print('It\'s False')


if 0:
    print('It\'s True')
else:
    print('It\'s False')

# Blocks in python is created/differentiated using indentation
# indentation: Leaving Tab space


age = int(input('Enter your age '))

if (age >= 18): 
    print('You can vote in the election')
else: 
    print('You cannot vote in the election')


# Conditional on list 

courses = ['Python', 'DBMS', 'DSA']
print(courses)

course_name = input('Enter Your course name ') 

# string cannot be compared to list, so falsy value 
if (course_name == courses): 
    print(course_name)

# in is used to loop in courses : IF course name is in list courses print name
if (course_name in courses): 
    print(course_name)

name = 'Python' 
user_name = input('Enter Name ')

if (user_name == name): 
    print ('Saanp paal rha tha')
else: 
    print ('Hello')

# Nested if & laddered if 
course_code = input('Enter your course code(Uppercase) ')

if (course_code == 'INT213'):
    print('Python')
elif (course_code == 'INT306'): 
    print('Database')
elif (course_code == 'CSE205'): 
    print('DSA')
else: 
    print('You are not learning')