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
    
