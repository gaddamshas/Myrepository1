num = int(input('Enter the number: '))
rev = 0
backupnum = num
while num > 0:
    t = num % 10
    rev = rev*10 + t
    num = num // 10
#print(rev)

if rev == backupnum:
    print('Palindrome')
else:
    print('Not a palindrome')



#Amstrong number

'''n = int(input('Enter a number: '))

bkp = n
d_cnt = 0

while n > 0:

    n = n // 10

    d_cnt += 1
#print(d_cnt)

n = bkp
sum = 0
while n > 0:

    rem = n % 10
    sum = sum + rem ** d_cnt
    n = n // 10

#print(sum)

n = bkp

if sum == bkp:
    print(f'{n} is a Amstrong number')
else:
    print(f'{n} is not a Amstrong number')'''

    

    
#Palindrome
'''String = input('Enter a String: ')
if String == String[-1::-1]:
    print('Palindrome')

else:
    print('Not a palindrome')'''
    
