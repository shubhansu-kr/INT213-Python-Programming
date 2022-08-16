from xml.dom.minidom import Element


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
    nums.append(int(input(f'Enter element {i}: ')))

numSquare = []
for i in nums:
    numSquare.append(i*i)

print(f'Square of {nums}: {numSquare}')


# WAP to check if name is present in the list or not

friends = ['Aman', 'Shiv', 'Ram', 'Adam']
name = input('Enter a name: ')

if (name in friends):
    print('Record found ')
else:
    print('Record not found')

