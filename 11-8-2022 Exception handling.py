try:
    
    n = int(input('Enter the numerator: '))
    d = int(input('Enter the denominator: '))

    div = n // d
    print(div)



except ZeroDivisionError:

    print('Denominator should not be zero')

except ValueError:

    print('Value shold be an integer')

except Exception:

    print('Something went wrong')

