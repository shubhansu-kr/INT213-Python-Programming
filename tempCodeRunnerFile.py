# Using comples data structures as parameters 

def studentDetails(student): 
    n = student['name']
    m = student['marks']
    print(f'The student {n} scored {m} marks')

student = {'name': 'ABC', 'section': 'K21GP', 'marks': 45}

studentDetails(student)