#  Consider a tuple a = (1, 2, 10, 6, 9). Reverse the tuple elements 
#  and print the tuples on the screen 

a = (1, 2, 10, 6, 9)

# Use list insert 
tupleList = []
for i in a: 
    tupleList.insert(0, i)  #Logic to reverse the list
c = ()
for i in tupleList: 
    temp = (i,)
    c += temp

print(c)

# Use a[:: -1]
b = a[::-1]
print(b)

# Consider a tuple num = (3 ,10, 4, 70, 54), unpack the tuple elements 
# ans print them on screen 
num = (3, 10, 2, 50, 23)
a, b, c, d, e = num

print (a, b, c, d, e)


# Consider two tuples a = (19, 2, 4) and b = (40, 50, 60) 
# Swap elements of both tuples 
a = (19, 2, 4)
b = (40, 50, 60)

temp = a
a = b
b = temp 
print (a, b)