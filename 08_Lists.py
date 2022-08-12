# Data Structures in Python 
""" 

1. List 
2. Tuple
3. Dictionary
4. Sets 

"""

# Data Structures are used to handle large and complex data 

# Lists 
from zoneinfo import available_timezones


studentName = ['Avinash', 'Avesh', 'Sunny', 'Vidit', 'Hridhanu']
print(studentName)

# We can easily add multiple data base 
avinashDetail = ['Avinash', 20, 'Phagwara']
print(avinashDetail)

for val in avinashDetail: 
    print (val)

print(avinashDetail[0], avinashDetail[1])

size = len(avinashDetail)
sizeArr = avinashDetail.__len__()

print ('')
print (size, sizeArr)
print ('')


# size will be exclusive in range: So no need to subtract 1
for i in range (0, sizeArr): 
    print(avinashDetail[i])

for i in range (0, size): 
    print(avinashDetail[i])

nums = [3, 5, 3, 6, 7, 4, 2, 8]

# len() -> Gives the length of the list 
size = len(nums)

# type() -> Gives the data type of object 
print (type(nums))

# List of List 
myList = [['Shawn', 18, 32324], ['Ram', 14, 345, 543], 'Trishit', ['Ajit', 19]]
print (myList)

# Accessing 2d lists 
print (myList[0][1])

for val in myList: 
    for value in val: 
        print(value)

for val in myList: 
    print (val)
# <class 'list'>

# Printing elements of list on the basis of type 
for val in myList: 
    if (isinstance(val, list)): 
        for value in val: 
            print (value)
    else: 
        print (val) 


# Append - Add one element to the end
myList.append('isinstance is used to compare object class')
print(myList)

# Extend - Add multiple element to the end
# Use list to insert multiple elements 
myList.extend([[3,4,3], [4,3,2]])
print(myList)

# Insert - Insert one element anywhere in between
myList.insert(2, ['Shubh', 19])
print(myList)

# Pop - Remove the last element  or specify the index 
myList.pop()
myList.pop(2)
print(myList)

# remove - Remove the first occurence 
myList.remove(['Shawn', 18, 32324])
print (myList)
