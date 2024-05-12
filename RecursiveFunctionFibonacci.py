#Fibonacci series using recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

nterms = int(input('Enter number of terms: '))

print('Fibonacci series is: ', end = ' ')
for n in range(nterms):
    if nterms <= 0:
        print('Please enter the positive integer')

    else:
        print(fibonacci(n),end = ' ')
