# List methods 

nums = [1,2,3,1,2,4]

# count(parameter) : Gives the frequency of element
print(nums.count(3))

# sort - By default: ascending order
nums.sort()
print(nums)

# sort - parameter: reverse = true for descending order
nums.sort(reverse=True)
print(nums)

# sorted - makes a copy of list and doesn't modify the orignal list
# sorted is a function: not a method 
sortedNums = sorted(nums)
print(sortedNums)

# clear: 
sortedNums.clear()
print (sortedNums)

# copy: 
sortedNums = nums.copy()
print (sortedNums)

sortedNums.clear()
sortedNums = nums
print (sortedNums)

# max, min, len - functions 
print (max(nums))
print (min(nums))
print (len(nums))

# Enumerate Functions: Used to print elements along with index 
enum = list(enumerate(nums))
print (enum)

print(type(enum[0]))

# i is the index and j is the value 
for i, j in enum: 
    print(i, j)


# Operators 
list1 = [2,4,5,3,6]
list2 = [4,2,6,5]

# Concatination
list2 = list1 + list2
print(list2) 

# replication
list2 = list2 * 3 
print (list2)

# in 
if 3 in list2: 
    print ('Yes')
else: 
    print('No')

# not in 
if 3 not in list2: 
    print ('Yes')
else: 
    print ('No')