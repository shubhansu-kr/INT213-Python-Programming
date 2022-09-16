class Student: 
    def __init__(self, name, age) -> None:
        self.name = 'ABC'
        self.age = 20

s1 = Student('Some', 34)

print(s1.name, s1.age)


class S1: 
    school = 'His'
    def __init__(self) -> None:
        self.m1 = 32
        self.m5 = 54
        self.m4 = 32
        self.m3 = 54
        self.m2 = 32
    
    def avg(self): 
        return (self.m1+self.m2+self.m3+self.m4)/4

    def schoolInfo(cls):
        print(cls.school) 



o1 = S1(43, 64, 34, 43, 23)
o2 = S1(54, 54, 34, 5, 34)

print(o1.avg())
print(o2.avg())

s1.schoolInfo() 