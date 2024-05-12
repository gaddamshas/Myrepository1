class A:
    
    def __init__(self,a):
        
        print('I am constructor from A')
        self.a = a
        

    def display(self): #same function is also avilable in child class, so displ
                       #ay function of class B overrides display fun of A 
        print('I am display function from A')

    def show(self):
        print('I am show function from class A')
        print('Value of a = ',self.a)


class B(A):

    def __init__(self,a): #First priority is given to child constructor
        self.a = a
        print('I am constructor from class B')
        super().__init__(a) #'super()'-->used to inherit instance varibles from 
                            #class A constructor
        
        

    def display(self): #Method overriding -->display function is avilable in parent class but child class display over
        print('I am display from class B')   #ride parent class

obj = B(10)   #'obj' is object for B-->'B' inherited properties from Class A
obj.display()
obj.show()
obj.display()

print(B.mro())#it is Method Resolution Order,which decides which is to be execu
              #ted first
