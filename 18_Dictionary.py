# Dictionary

# Empty dictionary 
m = {}

a = {'A': 20, 'B': 30, 'C': 40}
print(a)

print(a['A'])

b = {3: 32, 4: 44, 5: 55, 3: 33}
print(b)

print(b[3])

# get method 
print(b.get(4)) 

# If we access any key which is not a part of dictionary, 
# we get error in case of [] but if we use get() method 
# we will get none

if (b.get(100)): 
    print('T')
else:
    print('False')

# print(b[6]) : Error since key = 6 does not exist 
print(b.get(6)) #Prints None

s = [(1, 's'), (2, 'ds'), ('4', 324)]
t = dict(s)
print(t)

print('Input details')

x = input()


myDict = {}
myDict[0] = 'Avesh'

# print(myDict, myDict[2])  : Error: Key does not exist in the dictionary

# a is the key of dictionary
for a in t: 
    print (a, t[a])

# Assignment operator: Update the existing key else create a new key 
t[9] = 'Nine'
t[8] = 'Eight'

t['4'] = 'Four'

print(t)

# Update method: same as assignment
t.update({8: 'eight', 11: 'eleven'})
print(t)

# key: Returns a list of all the keys in the dictionary
print(t.keys())
for i in t.keys(): 
    print(i)

# values : Returns the list of all values in the dictionary 
print(t.values())
for i in t.values(): 
    print(i)

# item : Returns the list of all the items in the dictionary in form of tuples
# tuples can be easily unpacked 
print(t.items())
for i in t.items(): 
    print (i)

for i, j in  t.items(): 
    print (i, j)

# Converting list of tuple into dictionary 

a = [('name', 'Abc'), ('age', 25)]
listDictionary = dict(a)

print (listDictionary) 

