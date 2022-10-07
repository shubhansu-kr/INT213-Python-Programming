# Many Forms for one name

# 1. Operator overloading 
# 2. Method/function overloading
# 3. Method Overriding
# 4. Duck Typing

# Overloading means we have a same name function which we 
# can use different arguments 

# Overriding in case of inheritance, base and child class

# Operator overloading 
print(10 + 20)
print('10'+ '20')

# Every data type has a class defined, so + operator has a different meaning
# in interger class and different meaning in string class 

# interger overview 
# int.__add__(self, other): 
#     return self.val + other

# string overvied
# str.__add__(self, other): 
#    return self.val.append(other)

# This is an inbuilt function overloading

class A: 
    def sum(self): 
        print('Second sum method')

    # Which ever is written later is considered to be true 
    def sum(self, a):
        print('First Sum method', a)

obj = A()
obj.sum()
obj.sum(10)