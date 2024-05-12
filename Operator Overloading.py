#Operator Overloadind: Giving extara functiionality/feature to the operator.

class Quantity:

    def __init__(self,qty):

        self.qty = qty

    def display(self):

        print(self.qty)

    def __add__(self,other): #Here we are providing extra functionality to 'add'
                            #by using __add__
        return self.qty + other.qty

    def __gt__(self,other):
        if self.qty > other.qty:
            return True
        else:
            return False
    def __str__(self):
        return str(self.qty)


q1 = Quantity(35)

q2 = Quantity(25)

print(q1 + q2) #if don't provide extra functionality to operator(add) then it will
               #throw an error

print(q1 > q2)   #__add__/__gt__/__str__ etc are called as dunder/special/magi
                 #cal methods

print(q1)

