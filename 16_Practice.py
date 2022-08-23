# Take input from user to create a list of 10 elements 

inputArr = []

n = int(input('Enter the number of elements: '))

for i in range(0, n): 
    inputArr.append(int(input(f'Enter element {i+1}: ')))

print(inputArr)
tupleList = list(enumerate(inputArr))
print(tupleList)

# Take any two set and remove the common element from the two set adn 
# create a list of common elements 

a = set()
b = set()
n = int(input('Enter the number of element in set a: '))

for i in range (0, n): 
    a.add(int(input(f'Enter the {i+1} element: ')))

n = int(input('Enter the number of element in set b: '))
for i in range (0, n): 
    b.add(int(input(f'Enter the {i+1} element: ')))

c = (a | b)-(a & b)
print (c)

a = {1,2,3,4}
b = {3,4,5,6}
# or we can do this 
c = a.difference_update(b) 

print (c) 