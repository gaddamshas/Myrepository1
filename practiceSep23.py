#Check prime number
n = int(input('Enter tge number :'))
count = 0
i = 1

if n % 2 == 0 and n < 2:
    print('Not')
else:
    while(i<n):
        if(n % i == 0):
            count += 1
        i += 1

        if(count > 2):
            print('Not')

            break
    if(count == 2):
        print('Prime')
        
