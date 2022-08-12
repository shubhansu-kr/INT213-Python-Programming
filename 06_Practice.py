# WAP to calculate square of a number if it is greater than 5

num = int(input('Enter Num '))

if (num > 5):
    num_sq = num * num
    print(f'Square of {num} is {num_sq}')
else:
    print(f'Num ({num})is smaller than equal to 5')


# WAP to check whether a number entered by the user is a prime or not

num = int(input('Enter num (to check prime) '))
isPrime = True

if (num == 1):
    isPrime = False
else: 
    for i in range (2, num//2): 
        if (num % i == 0): 
            isPrime = False
            break
        
if (isPrime): 
    print(f'{num} is a prime number')
else: 
    for i in range (1, 11): 
        x = num * i
        print(f'{x} ')

