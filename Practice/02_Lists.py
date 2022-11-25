# Lists in python are arrays in JS. 

# Lists can store multiple data types in one file only

arr = [2, 8, 21, 44, 4, 5, 3, 3, 5, 'shubh']

# Methods. 

# len() Prints the number of element in the list 
print(len(arr))

# type() : <class 'list'>

# Access items: We can use indexing to access the elements.
# list has zero based indexing. as well as negative index just like slicing.

print(arr[0], arr[-1])

# We can also use slicing in lists. 
print(arr[1: 3]) # returns a list. 

# Modify elements. 
arr[1:3] = ['new', 'elements', 'inserted', 'splicing']
print(arr)

# insert functions. 
# arr.insert(index, val) 
arr.insert(0, 'first')
print(arr)

# append - insert at the end 
arr.append('end')
print(arr)

# extend. - Append an iterable object to list 
tup = ('hehe', 'this', 'is', 'a', 'tuple')
arr.extend(tup)
print(arr)

# remove('val'): Remove all the occurence of val 
arr.remove(3)
print(arr)

# pop(index): Remove the element at given index. 
arr.pop(4)
print(arr)

# del is used to delete an element or complete list. 

# del arr[0] : Deletes the arr[0] item 
# del arr : Deletes the arr 

# clear: clears the list, empty list still exists. 
# arr.clear()

# print(arr)

# List Comprehension. 
# newlist = [x+5 for x in arr if x > 5]

newList = [x for x in arr if isinstance(x, str)]
print(newList)
newList = [x for x in arr if isinstance(x, int)]
print(newList)


# Sort in ascending order. 
newList.sort()
print(newList)

# sort in descending order. 
newList.sort(reverse=True)
print(newList)

# Sorting using custom comparison
def myComp(n): 
    return abs(21-n)

newList.sort(key=myComp)
print(newList)

newList.reverse() # reverses the list.
print(newList)

