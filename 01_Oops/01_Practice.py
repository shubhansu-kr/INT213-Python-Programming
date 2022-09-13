# Create a class student, Attributes: Name, Age, Section 

class Student: 
    def __init__(self, name, age, section) -> None:
        self.name = name
        self.age = age
        self.section = section

    def display(self): 
        print(f'Name: {self.name},\nAge: {self.age}, \nSection: {self.section}')

s1 = Student('Shubhansu-kr', 19, 'K21GP')
s1.display()


# Create class bankaccount and create two methods: 
# withdraw and deposit 
class BankAccount: 
    def __init__(self, balance) -> None:
        self.balance = balance
    
    def withdraw(self, a): 
        if self.balance >= a: 
            self.balance -= a
            print('withdraw successfull')
        else: 
            print('Insufficient balance')

        print(self.balance)

    def deposit(self, a):
        self.balance += a
        print('Deposit Sucessfull')
        print(self.balance)

A1 = BankAccount(32111)
A1.deposit(889)
A1.withdraw(10000)

# Valid Parenthesis 
s = '()()()'

def isValidParenthesis(s): 
    list1 = []
    for i in s: 
        if (i == '(' or i == '{' or i == '['): 
            list1.append(i)
        else: 
            n = len(list1)
            if(n): 
                c = list1[n-1]
                if (i == ')' and c != '(' or i == '}' and c != '{' or i == ']' and c != '['): 
                    return False
                else: 
                    list1.pop()
            else: 
                return False
    return True 

print(isValidParenthesis(s))