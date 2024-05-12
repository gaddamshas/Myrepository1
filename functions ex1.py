#Treating the function as Object

def shout(a):
    return a.upper()
print(shout('Good Morning'))

wake = shout
print(wake('Hello, Good Morning'))


#Passing function as an arguement



def greet(fun):#passing function as arguement
    #storing the function in a variable
    greetings = fun('Hello, how are you?')
    print(greetings)

def shout(a):
    return a.upper()
def whisper(a):
    return a.lower()

greet(shout)
greet(whisper)


# Python program to illustrate functions
# Functions can return another function
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))
