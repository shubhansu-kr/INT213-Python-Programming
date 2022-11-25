# Tuples: NonMutable, Duplicates, Indexed. 

# creating tuple 
a = ()
b = (2,)
c = 4, 
d = 34 # not a tuple. 
print(type(a), type(b), type(c), type(d))

# Tuples can be accessed via indices. 

tup = (3, 4, 2, 4 , 3, 'shubh', 'kan')
print(tup[0], tup[-1], tup[5])

print(3 in tup, 1 in tup)

# Tuples are unmutable, so we cannot do any operation on tuple except 
# concatination of tuple

d = a + b + c
print(d) # a tuple.

# To modify tuple convert into list then modify and again convert back to tuple.

print (tup)

tup = list(tup)
tup.pop(3)
tup = tuple(tup)

print(tup)

# Unpacking of tuple. 
first, second, *third = tup 
print(first, second, third) #unpacks in a list. 

# multiply tuple : Multiply frequency. 
tup *= 2 
print (tup)

# count(): Returns the frequency of tuple. 

