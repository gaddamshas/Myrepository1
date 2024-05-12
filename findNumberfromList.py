li = [10,23,54,12,44,67,100,30]
num = int(input('Enter the number: '))
for i in range(0, len(li)):
    if li[i] == num:
        print(f'{num} found at index {i}')
        break
else:
    print('Number not found')

