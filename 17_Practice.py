# Take set of elements from user in a list 
# Remove the empty string from the list and return the resultant list.

from itertools import zip_longest


userInput = []

n = int(input("Enter the number of string: "))
for i in range (n):
    userInput.append(input(f'Enter string {i+1}: '))

print(userInput)
for i in userInput:
    if (i == ''): 
        userInput.remove(i)
        

print(userInput)


# From a list entered by the user, check the occurence of a specific element
# If it exists remove all its occurence;

x = input('Enter string to search: ')

while(x in userInput): 
    userInput.remove(x)
else: 
    print(userInput)

# Consider a tuple A and convert the elements into a string and print 
# the string on screen 

s = ''
A = ('This', 'is', 'a', 'python', 'lecture')
for i in A: 
    s += i + ' '

print(s)


# Consider 3 list, name , age and course. iterate over list and print result
name = ['A', 'B', 'C']
age = [10, 20, 30]
course = ['Python', 'database']

# import itertools
# for i ,j,k in itertools.zip_longest(name,age,course):
#     print(i,j,k)


i = 0
n = max(len(name), len(age), len(course))
print(n)
while (i < n):
    if (i < len(name)):
        print(name[i], end=' ')
    else: 
        print('Null', end=' ')
    if (i < len(age)):
        print(age[i], end=' ')
    else: 
        print('Null', end =' ')
    if (i < len(course)):
        print(course[i])
    else:
        print('Null')
    i = i+1


   
# Consider two set s1 and s2, remove the uncommon element present in both
# and store them in a tuple 
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

s3 = tuple((s1 | s2) - (s1&s2))
print (s3)



