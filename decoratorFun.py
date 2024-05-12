def decfun(f):

    def innerfun():
        
        print('*'*20)
        f()
        print('*'*20)
        
    return innerfun

#@decfun

 


@decfun

 
def show():

    print('I am show')

show()

def display():

    print('I am display function')

display()
