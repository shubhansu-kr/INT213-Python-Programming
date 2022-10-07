# Sets : Store data/collection 

# Sets are unordered in nature, we cannot use indexing
# No duplicacy of data: Only once occurence of one element

# Even if i add element more than once, element is only inserted once
a = {1, 5, 2, 2, 4}
print (a) 

# <class 'set'>
print(type(a))

# Type casting 
x = [1,3,2,5,3,5,4,6,7, 8]
y = (4, 2, 1, 5, 6, 3, 21)

w = set(x)
print(w)

z = set(y)
print(y)

# Dictionary and set have same curly braces 
# so to create an empty set, we have to type cast

a = {}
b = set({})

print (type(a)) # <class 'dict'>
print (type(b)) # <class 'set'>

# print (z[0]) Error: Cannot access the set element 

# We can though iterate using loops 
for i in z: 
    print(i)

# Methods in loops: 

print(z)

# add
z.add(3) # add already existing element
print(z) # No change in set

z.add(11) # add a new element
print (z) # new element inserted 

# remove
# z.remove(32) # Remove a non-existent element: Cannot remove (error)
print (z) # No change in set 

z.remove(3) # Removes the 3
print(z)

# discard
z.discard(32) # No error even if the element does not exist 
print(z) # Remove only if element is present 

z.discard(11)
print (z) #Removes the element 11 

# pop : Takes no argument: Remove any random element 
z.pop() 
print(z)

# issubset : Check if z is a subset of w and return a boolean result
isSubset = z.issubset(w)
print (isSubset)

# difference : Returns a subset which contains the difference of  two set
# elements which are present in only one set 

# Order matters: Element which are present is q but not in z 
q = w.difference(z)
print (q)

# Removes the common element of w and z 
q = w.difference_update(z)
print(q)

# intersection : Returns the intersection of two sets 
q = w.intersection(z)
print(q)

# union 
q = w.union(z)
print (q)

# issuperset : Returns boolean for if the set is a superset 
print(q.issuperset(w)) # q is a super set of w : true 
print(w.issuperset(q)) # w is a super set of q : false 

# isdisjoint : Check if both the sets are completely different 
print (q.isdisjoint(w))

# Functions in set 

# len 
print(len(q))

# sorted : Return a list of sorted element: Not a set: return a list 
print (q)
m = sorted(q)
print (m) 

# max 
print(max(q))

# min 
print (min(q))

# sum 
print (sum(q))

# enumerate 
m = list(enumerate(q))
print (m)

# operations in sets 

a = {1,2,3,4,5}
b = {4,5,6,7,8}

# union | 
c = a | b 
print (c)

# intersection & 
c = a & b 
print (c) 

# difference - 
c = a-b 
print (c)

c = b-a 
print(c)

# to check subset => <= 
c = a|b 

# symmertric difference ^ : ((Only in a) union (only in b)) 
# to check the existence of element in/not in

