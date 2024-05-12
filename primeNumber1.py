lower = 1
higher = 1000
list = []
print(f'Prime numbers between {lower} and {higher} are: ')
for num in range(lower,higher+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                
                break
        else:
            list.append(num)
print(list)
