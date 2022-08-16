# WAP to find the max of all the Element in a list

nums = [23, 43, 56, 10, 3, 72]

myMax = -10e9
for i in nums:
    if (myMax < i):
        myMax = i

print(f'Maximum Number in {nums} is {myMax}')


# WAP to find the square of all the numbers in the list
nums = []

n = int(input('Enter The number of elements: '))
for i in range(0, n):
    nums.append(int(input(f'Enter element {i+1}: ')))

numSquare = []
for i in nums:
    numSquare.append(i*i)

print(f'Square of {nums}: {numSquare}')


# WAP to check if name is present in the list or not

friends = ['Aman', 'Shiv', 'Ram', 'Adam']
name = input('Enter a name: ')

name.lower()

for i in range (0, len(friends)): 
    friends[i] = friends[i].lower()

if (name in friends):
    print('Record found ')
else:
    print('Record not found')

# WAP to create a list from user input

n = int(input('Enter number of elements: '))
userList = []
for i in range (0, n): 
    userList.append(int(input(f'Enter element {i+1}: ')))
print(f'userList: {userList}')

# str.lower()
# str.upper()
# str.capitalize()

# MAX value in python is retrieved using sys module 

import sys 


maxINT = sys.maxsize
minINT = -(sys.maxsize)
longINT = sys.maxsize + 1 

print (f' maxINT: {maxINT} \n minINT: {minINT} \n longINT: {longINT}')