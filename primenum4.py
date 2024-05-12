count = 0
div = 1
num = int(input('Enter the number: '))
if num > 2 and num % 2 == 0:
    print('Not a prime number')

    while num >= div:
   
        if num % div == 0:
            count += 1
       #print(count)
        div += 1

    
        
    if count == 2:
        print('Prime number')
else:
    print('Not Prime number')

