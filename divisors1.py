num = int(input('Enter the number:'))
div = 1
count = 0
while div <= num:
    if num % div == 0:
        count += 1
        print(div)
    div += 1
print('Total number of divisors =',count)


