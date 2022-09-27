class Student: 
    # Data Memebers 
    roll = 0
    name = ''
    section = ''

    def __init__(self, name) -> None:
        self.name = name
    
    # Member function
    def speak(self): 
        print(f' Name: {self.name}\n Roll: {self.roll}')


s1 = Student('shubh')
s2 = Student('Ron')


print(s1.name)
# Both have the same roll 0 as assigned default by the student class 
print(f'Ron\'s roll is {s2.roll}, shubh\'s roll is {s1.roll}')

# We can change the default values 
s2.roll = 21
s1.roll = 33 
print(f'Ron\'s roll is {s2.roll}, shubh\'s roll is {s1.roll}')

# We can call the member function of the class in two ways
# pass object as parameter or use object to call the function
s1.speak()
Student.speak(s2)


# Single level inheritance 
class Marks(Student): 

    percent = 0
    grade = 'A'

    def __init__(self, name, percent, grade) -> None:
        super().__init__(name)
        self.grade = grade
        self.percent = percent

    def speak(self): 
        self.section = 'GP'
        print(f'{self.name} {self.roll} {self.section} {self.percent} {self.grade}')

m1 = Marks('Avesh', 88, 'O')
m1.speak()

# Single level Inheritance 
# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		# print("My name is {}".format(self.name))
		# print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()

