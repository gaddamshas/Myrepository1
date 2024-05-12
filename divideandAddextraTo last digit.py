num = int(input('Enter the number: '))

extra = num % 4
secCount = (num - extra) // 4
print('A = ', secCount)
print('B = ', secCount)
print('C = ', secCount)
print('D = ', extra + secCount)
