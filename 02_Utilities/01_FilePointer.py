# Locate the file pointer and set the pointer.

# tell(): gives a num output: position of file pointer from the first char 
# filePointer.tell()

f = open('dummy.txt', 'r')

# Initially the pointer is at zeroth position 
print(f.tell())   # 0
content = f.read()

# After reading the file the pointer goes to the last char
# and then tells the last pointer pos. 
print(f.tell())   # 57


# Print the content of file(54 char)
print(content)

print()
print('Time to seek ')
print()
# seek(): Sets the file pointer in the file, takes an int argument and sets 
# the pointer n chars from the beginning. 

# Set the pointer 6 char away from beginning
f.seek(6)
print(f.tell())
content = f.read()

print(f.tell())
print(content)