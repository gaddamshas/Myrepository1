def addition(a,b):

    c = a + b
    print(f'addition of {a} and {b} is {c}')

def substraction(a,b):

    c = b - a
    print(f'Substraction of {b} and {a} is {c}')


def multiplication(a,b):
    
    c = a * b
    print(f'mul of {a} and {b} is {c}')

    
def fundamentalOp(a,b):
    c = b / a
    addition(a,b)
    substraction(a,b)
    multiplication(a,b)

    print(f'div of {b} and {a} is {c}')


fundamentalOp(15,30)
