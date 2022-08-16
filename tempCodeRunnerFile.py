n = int(input('Enter number of elements: '))
userList = []
for i in range (0, n): 
    userList.append(int(input(f'Enter element {i+1}: ')))
print(f'userList: {userList}')