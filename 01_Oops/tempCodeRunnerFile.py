s = '()[()([]){]'

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