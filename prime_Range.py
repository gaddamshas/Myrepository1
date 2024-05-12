#lr = int(input('Enter the lower range: '))
#ur = int(input('Enter the upper range: '))


'''for num in range(lr, ur):
    cnt = 0
    for i in range(2,(num//2)):
        if num % i == 0:
            cnt += 1
            break

    if(cnt == 0 and num > 1):

        print(num, end = ' ')


for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')'''

for num in range(1,101):
    if num > 1:
        
        for i in range(2, num):
           
            if(num % i == 0):
                break
        else:
            print(num, end = ' ')


