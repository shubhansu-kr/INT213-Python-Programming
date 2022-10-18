import pickle
import os 

class Student: 
    def __init__(self, name, section, roll) -> None:
        self.name = name 
        self.section = section 
        self.rollNo = roll 
    
    def display(self): 
        print(self.name, self.section, self.rollNo)

lst = [Student('Vidit', 'GP', '54'), Student('Avi', 'GP', '21')]
f = open('dummy.txt', 'ab')

for i in lst: 
    pickle.dump(i, f)
f.close()

data = []
f = open('dummy.txt', 'rb')
n = os.path.getsize('dummy.txt')

while(f.tell() < n):
    data.append(pickle.load(f))

print(data)

for i in data: 
    i.display()