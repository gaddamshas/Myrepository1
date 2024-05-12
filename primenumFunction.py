def isPrime(num):

    count = 0
    div = 1

    #if num % 2 == 0:
        #print(f'{n} is not a Prime number')

    while num >= div:
        if num % div == 0:
            count += 1
        div += 1

    if count == 2:
        return True
    else:
        return False

# = int(input('Enter the number: '))
#res = isPrime(n)
#if res:
 ##else:
  #  print(f'{n} is not Prime number')

for i in range(1,1001):
    if isPrime(i):
        print(i,end=' ')
        
    
