# #  Methods in dictionary


myDict = {5: 25, 6: 36, 7: 49, 8: 64}

# copy(): As the name suggests, returns a copy of dictionary
dictCopy = myDict.copy()
print(myDict, dictCopy)

# pop(): Removes the pair with given key, if the given key does not exit: error
# Expects atleast one key 
myDict.pop(5)
print(myDict)

# myDict.pop(5) : Error
# print(myDict) : Error 

# popitem(): Removes the last pair takes no argument
myDict.popitem()
print(myDict)

# clear()
myDict.clear()
print (myDict)

myDict = dictCopy.copy()
print (myDict)

# fromkeys(): takes an iterable list and copies the value from dict
newDict = myDict.fromkeys([5,7, 0], 1)
print(newDict, type(newDict))

# get(): get the value 
x = myDict.get(100)
print(x) # none since the key 100 does not exist 

# del()


# update()
# keys()
# values()
# items()

# Convert two list into a  dictionary 
a = [2, 4, 5, 6, 3]
b = ['asdf', 'sfad', 'gfd', 'fgs', 'dfger']

dict1 = {}
for i in range(0, len(a)): 
    dict[a[i]] = b[i]

print(dict1)

# Merge two dictionary in one 
dict2 = {9: 'shuf', 4: '434', 1: 'sfdag'}
for i in dict2: 
    dict1[i] = dict2[i]

print(dict1)

# Write a code to find the key in a dictionary with a min. val 
minKey = -1
minVal = 1e9

for i in dict1: 
    if (minVal > dict1[i]): 
        minVal = dict[i]
        minKey = i

print("MinKey: ", minKey)

# Create a dictionary using dictionary comprehension where each value 
# of a key in its square 

dictSq = {x: x*x for i in range(10)}