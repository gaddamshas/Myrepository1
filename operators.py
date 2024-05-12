print("1.Addition")
print("2.Substraction")
print("3.Fractional Division")
print("4.Multiplication")
print("5.Decimal value")
print("6.Power")
print("Which of the above operation is to be performed?")
n=int(input())

while(n <= 6):
    num1=int(input("Enter first value: "))
    num2=int(input("Enter second value: "))
    if(n==1):
        sum=num1+num2
        print("Sum =",sum)
        #print(" ")
        break
    
    elif(n==2):
        #num1=int(input("Enter first value: "))
        #num2=int(input("Enter second value: "))
        val=num1-num2
        print("Value =",val)
        #print(" ")
        break
   
    elif(n==3):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
        val=num1/num2
        print("Fractional Value =",val)
        #print(" ")
        break
    
    elif(n==4):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
        val=num1*num2
        print(num1,"*",num2,"=",val)
        #print(" ")
        break

    elif(n==5):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
        val=num1//num2
        print("Decimal value",val)
        #print(" ")
        break

    elif(n==6):
    #num1=int(input("Enter first value: "))
    #num2=int(input("Enter second value: "))
        val=num1**num2
        print(num1,"Power",num2,"=",val)
        #print(" ")
        break
#else:
print("Selected operation doesnot exists")

  
