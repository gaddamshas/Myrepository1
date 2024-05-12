for num in range(10, 10000):
    #num = 125
    sum = 0
    backup = num
    digits = []

    while num > 0:
        digits.append(num % 10)
        #sum = sum + r ** 3
        num = num // 10
       

    #print(sum," ",backup," ",sum==backup)
        
    for a in digits:
        sum = sum + a**len(digits)

    if sum == backup:
        print(sum)
