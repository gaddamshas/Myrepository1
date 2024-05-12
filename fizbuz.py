#num = int(input("Enter the number: "))
import random
num = random.randint(1, 100)
print(num)
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
if(num % num1 == 0 and num % num2 == 0):
    print("FIZ BUZ")
elif num % num1 == 0:
    print("FIZ")
elif num % num2 == 0:
    print("BUZ")
else:
    print("Number not divisible by", num1, "OR", num2)
