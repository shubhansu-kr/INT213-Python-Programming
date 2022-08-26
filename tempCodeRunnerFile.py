import itertools
name = ['A', 'B', 'C']
age = [10, 20, 30]
course = ['Python', 'database']

# for i ,j,k in itertools.zip_longest(name,age,course):
#     print(i,j,k)


i = 0
n = max(len(name), len(age), len(course))
print(n)
while (i < n):
    if (i < len(name)):
        print(name[i], end=' ')
    else: 
        print('Null', end=' ')
    if (i < len(age)):
        print(age[i], end=' ')
    else: 
        print('Null', end =' ')
    if (i < len(course)):
        print(course[i])
    else:
        print('Null')
    i = i+1

