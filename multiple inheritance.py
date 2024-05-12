#MULTIPLE INHERITANCE

class A:

    def __init__(self,a,b):#this constructor is overidden by child class constr
        self.a = a
        self.b = b
    
    def display(self):

        print('I am display function from Parent class A')

class B:

    def show(self):
        print('I am show function from Parent Class B')

    def display(self):
        print('I am disply function from Parent Class B')


class C(B,A): #The order of inheritance is important in multiple inheritnce
              #if same function is present in two different classes then-->
              #if we inherit the order C(A,B) then methods of class A overrides
              #class B, if we inherit C(B,A) then the methods of class B overr
              #ides methods of class A

    def __init__(self,c):
        self.c = c


    def info(self):
            
        print('I am info from Class C')

    def display(self):#priority will be given to child class method -->Method
                      #overriding
        print('I am display from class C')

a = C(10)

a.display()
a.display()
a.show()
a.info()
print(C.mro())
    
