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