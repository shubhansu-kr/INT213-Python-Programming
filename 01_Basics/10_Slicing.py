# SLicing string 

name = "Python Programming"

# Print name[2], name[3] -- 4 is excluded 
print(name[2:4])

# Print first 5 element 
print(name[:5])

# Print first 50 length: if range specified is larger than container size
# It prints the complete string 
print(name[:50])

# Print the element from 5th to last 
print (name[5: ])

# Negative represents reverse listing 
print (name[-4: ])

print(name[: -4])

# Range must be in ascending order, we cannot access list [5: 3] --> incorrect
# Similarly Reverse listing should also be in order 

print (name[-3: -1])  # Correct
# print (name[-3: -5])  # Incorrect

""" 
    List Slicing
"""

myList = [4, 3, 2, 5, 7, 5]

print(myList) 
print(myList[1: 5])
print(myList[:]) # Skips the last element 

slicedList = myList[1: 5]
print(slicedList)