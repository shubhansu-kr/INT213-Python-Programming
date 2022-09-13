# Classes and Objects 

# class keyword is used to declare a class 
class Student: 
    def config():
        print('i7 16GB 1TB')
    def config1(p): 
        print('i8')

    # self is a self refrencing pointer like this in cpp
    def config2(self): 
        print('i0')

# To create an object we call a constructor of class
s1 = Student()

# We can access the member function of class using class name 
Student.config()

# Pass a parameter
Student.config1('h')

# Object as a parameter 
Student.config2(s1)

# if we call the function having self as a parameter through an object of the 
# class we dont need to pass any parameter: 
# For example: 
s1.config2() 

# Size of an object: sum of memory size of all the data members;

# memory representation: 
# stack 
# heap
# Global var & static var
# Executables;

# The objects are stored in the heap memory 

# Constructor: __init__ 
class Teacher: 
    def __init__(self) -> None:
        print('Init function is used as constructor')
    def config(): 
        print('Dummy function ')

t1 = Teacher()
# init function is called whenever we create an instance of the class 

class Unit1: 
    def __init__(self, cpu, ram) -> None:
        pass
        self.a = cpu 
        self.b = ram 
    def config(self): 
        print(f'Cpu: {self.a}, Ram: {self.b}')

u1 = Unit1('i4', 43)
u2 = Unit1('i9', 43)

u1.config()
Unit1.config(u2)

