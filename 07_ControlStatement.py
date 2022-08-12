# break, continue, else with loop

str = 'Python'
for i in str: 
    if (i == 't'): break
    else: print (i)

for i in str: 
    if (i == 't'):
        continue
    print(i)

counter = 0


# ELse with loop 
while counter < 5: 
    print('Inside loop', counter)
    ++counter
else: 
    print('Outside Loop, Inside else')
    print(counter)

