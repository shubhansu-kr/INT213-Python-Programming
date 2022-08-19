# Tuples 

tuple1 = ()
print(tuple1)

# Homogeneous data : List 
# Hetrogeneous data : tuple 
tuple2 = (1, 2, 5, 7, 8, 8, 'sh', 'dsk')

print (tuple2)

# Tuples are immutable/unmodifiable, whereas list are mutable/modifiable

# We can create tuples without parenthesis : Tuple packing 
tuple4 = 1,4
print (tuple4)

# Tuples identification 
tuplesa = ('Shubh') 
tuplesd = 'shubh'
tuplesc = ('Shubh', )
tuplesb = 'Shubh' ,

# Destructuring of tuples 
a, b = tuple4
print(a)
print(b)

tuple11 = (3, 4, 3, [4,3])
print (tuple11[2]) #Prints 3 

# Let's try to update any value 
# tuple11[2] = 2   -----> Error: cannot modify the tuple  
# print (tuple11)

# Only modification allowed in tuple is concatination
tuple11 += tuple2
print (tuple11)

# Lets try to modify list within tuple : Yes it is possible
tuple11[3][1] = 101 # Noerror 
print (tuple11)