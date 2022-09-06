# Destructure of arguments 

fruits = 'Apple', 'Orange', 'Papaya'
print (fruits) # tuple 

# def demo (*args): 
#     print(args)

def demo (*anyName): 
    print(anyName)

demo ('Apple', 'Orange')

def demo (**kwargs): 
    print(kwargs) #dictionary 

demo(first = 'one', second = 'two') 

def isEven (list1): 
    evenList = [i for i in list1 if (i % 2 == 0)]
    return evenList

evenList = isEven([3,2,4,6,5,8,5,2])
print (evenList)


# Write a function to create and return a list where the resultant list 
# will have unique elements from the original list 
def isUnique (list1): 
    a = set(list1)
    return list(a)

uniqueList = isUnique([3,2,4,6,5,8,5,2])
print(uniqueList)

# Write a function that will reverse a four digit number
def reverseNum (num): 
    s = str(num)
    s = s[::-1]
    return int(s)

print(reverseNum(4352425))

# WAP that will take list as an input and will return the sum of alternate values in the list
def altSum(list2): 
    sum = 0
    flag = 1
    for i in list2: 
        if (flag): 
            sum = sum + i
            flag = 0
        else: 
            flag = 1
    return sum 

print(altSum([4,5,3,2,6,4,6,4]))