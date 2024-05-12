num = int(input('Enter the number: '))

div = 1
count =0
if num > 1:
    while div <= num:
        if num % div == 0:
            count += 1
        div += 1

        if count > 2:
            print('not a prime number')
            break
    else:
        print('Prime number')
