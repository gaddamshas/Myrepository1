'''num = int(input('Enter a number:'))
#
backup = num
count = 0

while num > 0:
    count += 1
    num = num // 10
#print(count)

sum = 0
num = backup
while num > 0:
    t = num % 10
    sum = sum + t ** count
    num = num // 10
#print(sum)
 
if backup == sum:
    print('Entered numer is Amstrong number')
else:
    print('Entered number is not Amstrong number')'''

'''num = int(input('Enter the number: '))
cnt = 0
bkp = num
while num > 0:
    cnt += 1
    num = num // 10
#print(cnt)

num = bkp
sum = 0
while num > 0:
    t = num % 10
    sum = sum + t ** cnt
    num = num // 10

if bkp == sum:
    print('Amstong')
else:
    print('not amstrong')'''

for num in range(100,999):

    bkp = num
    sum = 0
    while num > 0:
        t = num % 10
        sum += t ** 3
        num //= 10

        if sum == bkp:
            print(sum)
        
    
