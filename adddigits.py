# Sum of digits in the given number
'''num = int(input("Enter any number: ")) #153
sum = 0
while num > 0:
    t = num % 10  # t = 153 % 10 = 3 15 % 10 = 5
    sum = sum + t #sum = 0 3= 3  3 5=8
    num = num // 10 # num = 153 // 10 =15, 15//10 = 1
print(sum)'''

num = 1254234565656
i = 0
sum = 0
while num > 0:

    t = num % 10
    
    sum += t

    num = num // 10

    i += 1
print(f'the sum of digits in the given number = ', sum)
print('number of digits =',i)


    
