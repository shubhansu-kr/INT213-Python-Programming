class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

num1 = int(input())
num2 = int(input())

# Add two numbers 
sum = num1 + num2
print(sum)

# subtract numbers: let num1 > num2
diff = num1 - num2
print(diff)

# remainder 
rem = num1 % num2 
print(rem)

# normal div: Quotient
q1 = num1 / num2 
print(q1) 

# integer div: Quotient 
q2 = num1 // num2 
print(q2)

# Multiply 
prod = num1 * num2 
print(prod)