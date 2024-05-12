#eg1
def display():        #Closure : Remembering the state of local variable and 
    x = 10            # executing from outside the function. Here 'x' is local 
    #print(x)          # variable and InnerFun using it as non local variable and
                      # executing it from outside the function

    def InnerFun():
        print(x)

    #InnerFun()
    return InnerFun


fun = display()
fun()


#eg2

def Show():
    y = 20
    #print(y)

    def innerFun():
        print(y)
    return innerFun



f = Show()
#print(y)
f()
