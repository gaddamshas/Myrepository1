def decoratorFun(fun): # here 'f' is original function--> display

    def innerFun():
        print('*'*10,'I am inner function of decorator function','*'*10)
        fun()  #calling original function
        print('*'*10, 'End of inner function','*'*10)
        
    return innerFun

@decoratorFun

def display():
    
    print(' '*10,'I am main display',' '*10)

display()

'''class Campus:
    def __init__(self):

        self.course = 'Campus preperation'
        self.duration = ' 2 months'

    def info(self):

        print('COURSE:', self.course)
        print('DURATION', self.duration)

obj = Campus()
obj.info()'''

