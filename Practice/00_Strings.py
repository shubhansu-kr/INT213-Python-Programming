s = 'shubhansu kumar singh' 

# strings are array of characters. 

print(s[0])

# for c in s: 
#     print(c)

# len - len(c): Returns the length of the string. 
print(len(s))

# in is used to find the substring 
print('si' in s) # true. 

# not in is used to check if substring is not present. 
print('si' not in s) # false 

# String Slicing.
# 
# [a:b] -> string is sliced from index a to b-1. 
# By default, a value is 0 and b value is len of string. 

print(s[:]) # 0 to 20 index. 
print(s[:9]) # 0 to 8 index. 
print(s[9: ]) #  9 to last index (20)

# Negative indexing. 
# Last index is -1 and first index is -len 
# Prints in forward order. 
print(s[-21: -12]) 

# Modifying methods.
# Upper() : Put char to uppercase.  
print(s.upper())
print(s.lower())

# strip(): Remove whitespaces from start and end of the string. 
print('  sh '.strip()) # prints sh only

# replace('x', 'y'): Replace x with y
print('Heppo'.replace('p', 'l'))

# split(): Use to divide string into substrings and returns a list. 
print(s.split('u'))

# concatination 
print(s + ' hola')

# format strings: Format is used to insert string in between 
st = 'i will insert something here {}'
print(st.format(21))

p = 21
st = f'num is {p}'

print(st)

# Methods: 

# count(): Returns the frequency of argument in string
print(s.count('s'))