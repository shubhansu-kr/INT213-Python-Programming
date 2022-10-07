# Looping Constructs 

# While Loop 

isLearning = True

while (isLearning): 
    course_code = input('Enter your course code(Uppercase) ')

    if (course_code == 'INT213'):
        isLearning = course_code
    elif (course_code == 'INT306'): 
        isLearning = course_code
    elif (course_code == 'CSE205'): 
        isLearning = course_code
    else: 
        isLearning = False 

# For loops in python 

for i in range (10):
    print (i) # [0, 10)
for i in range (2, 10):
    print (i) # 10 is excluded 
for i in range (2, 10, 3): 
    print (i) # start from 2, end at 10, increase by 3

# TO decrement, we can use negative factor 
for i in range (10, 2, -1):
    print (i)

str = 'Python Programming'
for index in str: 
    print(index)

