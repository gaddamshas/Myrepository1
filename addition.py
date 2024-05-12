num1=int(input("Enter first value: "))
num2=int(input("Enter second value: "))
n=int(input("What operation to be performed?1.add 2.sub 3.div 4.mul: "))
if(n==1):
    sum=num1+num2
    #break
    print("sum =",sum)
    print(" ")
    

elif(n==2):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
    val=num1-num2
    #break
    print("Valu e=",val)
    print(" ")
   
elif(n==3):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
    val=num1//num2
    #break
    print("Valu e=",val)
    print(" ")
    
elif(n==4):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
    val=num1*num2
    #break
    print("Value =",val)
    print(" ")

else:
    print("Invalid key")

  
