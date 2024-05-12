'''num = int(input('Enter the number: '))
if num > 2 and num % 2 == 0 :
    print('Not a Prime number')

else:

    div = 1
    count = 0

    while div <= num:
        if num % div == 0:
            count += 1

        if count > 2:
            #print('Not a prime number')
            break
        div += 1

    if count > 2:
        print('not Prime number')
    else:
        print('Prime number')'''




'''def primeFun(n):
    div = 1
    count = 0
    if(n > 2 and n % 2 == 0):
        print('Not a prime number')

    else:
        while n > div:
            if(n % div == 0):
                count += 1
            if count > 2:
                print('Not a prime number')
                break
            div +=1        
        else:
            print('Prime number')'''
#lower = int(input('lower: '))
#higher = int(input('higher: '))
'''for num in range(1, 1001):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end = ' ')'''

'''x = 0
y = 1
n = int(input('Enter the number you want as fib'))
#terms = int(input('Enter number of terms: '))
#print('Fibonaccie series is: ')
#print(x, y, end=' ')
for i in range(2, 1000):
    z = x + y
    #print(z, end = ' ')
    x = y
    y = z
    if i == n:
        break
print(z)'''

'''def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n - 2))

nterms = int(input('Enter n terms:'))
if nterms > 0:
    print('Fib series is:')
    for i in range(nterms+1):
        print(fib(i))
else:
    print('Enter positive number')'''
        
   
        
        
'''def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))
n = int(input('Enter the n: '))
if n >= 0:
    for i in range(n+1):
        print(fib(i))

else:
    print('Enter positive number')'''
'''from abc import ABC, abstractmethod

class Animal(ABC):
    def sounds(self):
        pass

class Dog(Animal):

    def sounds(self):
        print('bow boww')
        
class Cat(Animal):
     def sounds(self):
         print('Meow meow')



c1 = Cat()
c1.sounds()
d1 = Dog()
d1.sounds()'''

try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ValueError:
    print('Value is not correct')
    
except ZeroDivisionError:
    print('Denominator should not be zero')
    
except Exception:
    print('Something went wrong')

finally:
    print('Closing')



