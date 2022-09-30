# Create a class names 'Person' with details of person like name, 
# age and address. 
# Create another class company which has the details of the company like name, location, deals with
# Create another class employee which will inherit the details of both 
# Person and Company 
# Print the details of an employee with its name, age, address, company, 
# designation and salary 

class Person: 
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age 

class Company(Person): 
    def __init__(self, name, age, worksWith, location) -> None:
        super().__init__(name, age)
        self.worksWith = worksWith
        self.location = location

class Employee(Company): 
    def __init__(self, name, age, worksWith, location, des, sal) -> None:
        super().__init__(name, age, worksWith, location)
        self.salary = sal
        self.designation = des

    def details(self): 
        print(
            f"""
            Name        :   {self.name}
            Age         :   {self.age}
            WorksWith   :   {self.worksWith}
            Location    :   {self.location}
            Designation :   {self.designation}
            Salary      :   {self.salary}
            """
        )

e = Employee('shubhansu-kr', 19, 'Micro', 'Hyderabad', 'L4', 4243454)
e.details()
