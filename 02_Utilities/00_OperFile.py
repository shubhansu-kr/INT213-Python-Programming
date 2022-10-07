# w - used to open file in writing mode  || Text mode 

# What is f? If dummy is not available, py creates one 
f = open("dummy.txt", 'w')

# Write the file in append mode 
f.write("Hello\n")

f.write('Python')
f.close()

# Open the file in read mode 
f = open('dummy.txt', 'r')
print(f.read())
f.close()

# ----------------------------------------------------------------

# Open the file in read mode : rb tells to read in binary mode
# To read a file, the file should exist 
f = open('dummy.txt', 'rb')
print(f.read())
f.close()

# ----------------------------------------------------------------

# Open("filePath", mode, buffer, encoding, error)
# Default mode is read mode 

f = open('dummy.txt')
print(f) #<_io.TextIOWrapper name='dummy.txt' mode='r' encoding='cp1252'>
f.close()

# f.closed() Tells if file is closed or not 
# f.writable() Tell if we can write into the file 
# f.name() Tells the name of the file f is binded to 
# f.writelines() we can add a tuple, dict or any complex data

# Writing into a file : Prev contets get overwritten
f = open('dummy.txt', 'w')

# f contains the refrence to the dummy file, we can operate f and reflect 
# the changes in dummy file 

f.write('Let\'s write something\n')
lis = ['FirstLine', 'SecondLine', 'ThirdLine']

# We can loop through the list to manipulate the entry
for i in lis: 
    f.write(i)
    f.write('\n')