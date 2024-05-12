#Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

nterms = int(input('Enter number of terms:'))

print('Fibonacci series is: ',end = ' ')
for i in range(nterms):
    if nterms <= 0:
        print('Please Enter Positive integer')

    else:
        print(fibonacci(i),end = ' ')
        
##Factorial
'''def factorial(n):
    if n == 1:
        return n
    else:
        return (n * factorial(n-1))

num = int(input('\n\nEnter the number: '))

print(factorial(num))'''
