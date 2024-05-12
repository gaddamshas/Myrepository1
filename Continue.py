num = int(input('Enter number:'))
i = 0
while i <= num-1:
    i += 1
    print(f'Iteration {i} started')
    if i % 2 == 0:
        continue
    print(f'Iteration {i} ended')
