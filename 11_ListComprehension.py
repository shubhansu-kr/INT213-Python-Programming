# List Comprehension

Arr = [4, 3]
nums = [4, 3, 56, 3, 5, 3, 22]

# Creates an array of same length as nums with arr[i] = nums[i] ** 2
Arr = [i ** 2 for i in nums]
print(Arr)


Age = [32, 54, 65, 23, 16, 23, 54, 23]
friendAge = [f'My Friend is {i} year old' for i in Age if(i < 30)]

print(friendAge)
