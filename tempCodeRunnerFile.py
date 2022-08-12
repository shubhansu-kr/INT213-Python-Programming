num = int(input('Enter num (to check prime) '))
isPrime = True
for i in range (2, num//2): 
    if (num % i == 0): 
        isPrime = False
        

if (isPrime): 
    print(f'{num} is a prime number')
else: 
    for i in range (1, 11): 
        x = num * i
        print(f'{x} ')