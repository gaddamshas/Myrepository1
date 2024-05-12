num = int(input("Enter any number: ")) #153
sum = 0
while num > 0:
    t = num % 10  # t = 153 % 10 = 3 15 % 10 = 5
    sum = sum + t #sum = 0 3= 3  3 5=8
    num = num // 10 # num = 153 // 10 =15, 15//10 = 1
print(sum)
    
    
    
    
