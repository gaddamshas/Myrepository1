x = 0
y = 1
#print("Enter the range")
num = int(input("Enter how many terms you want: "))
print("The Fibonacci seris is : ", end = " ")
print(x, y, end = " ")
#i = 3
#while i <= num:
for i in range(2,num): #
    z = x + y       # 0,1 0+1, 1+1, 1+2,3+2,5+3,8+5,13+8,21+13,34+21
    print(z, end = " ")
    x = y
    y = z
    #i += 1

    
   
'''x = 0
y = 1
print(x,y,end = ' ')
i = 3
n = 10
while i <= n:
    z = x + y
    print(z,end =' ')
    x=y
    y=z
    i += 1'''
    
