import os 
f = open('dummy.txt', 'rb')

n = os.path.getsize('dummy.txt')
print(n)
print(f.tell())
print(f.read())
print(f.tell())