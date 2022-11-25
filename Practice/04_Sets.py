# set : unchangable Noduplicates Noindexing

st = {3, 3, 2, 4, 65, 4 , 934}
print(st)

# Since we cannot access elements using indexing only way left is 
# through loop 

for i in st: 
    print(i, end=' ')

print(21 in st)

# Adding item to the set: function used is add 

st.add('hello')
print(st)

newSet = {'this', 'is', 'a', 'new', 'set'}
lis1 = ['32', '32', '43']

st.update(newSet)
print(st)

st.update(lis1)
print(st)

st.remove('32')
print(st)

# st.remove('something that does not exist')
# print(st): Gives error since item does not exist. 

# use discard() to remove item if not sure 
st.discard('something')
# no error
print(st)

st.pop() #remove last element: any item is removed. 
print(st)


# Join sets

st.union(newSet)
st.intersection(newSet)
st.symmetric_difference(newSet)
