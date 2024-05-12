class My_class: #Class can be created only using keyword 'class'              

    def __init__(self,num1,num2): #__init__--->is a constructor

        self.a = num1              #Instance Variables, these can be accessed 
        self.b = num2              #only be creating object

    #def show(self):
       
        #print(self.num1,self.num2)


   # def display(self):
        #print('I am display from class Myclass')



    def addition(self):

        c = self.a + self.b
        #print(c)
        return c

        
    def substraction(self):

        c = self.a - self.b
        #print(c)
        return c


    def multiplication(self):

        c = self.a * self.b
       # print(c)
        return c

    def division(self):

        c = self.a / self.b
        #print(c)
        return c


obj1 = My_class(27,13)

add = obj1.addition()
print(add)

sub = obj1.substraction()
print(sub)


mul = obj1.multiplication()
print(mul)


div = obj1.division()
print(div)


#obj1.show()
#obj1.display()
#print(id(obj1))


obj2 = My_class(76,64)

add2 = obj2.addition()
print(add2)

sub2 = obj2.substraction()
print(sub2)

mul2 = obj2.multiplication()
print(mul2)

div2 = obj2.division()
print(div2)
#obj2.show()
#obj2.display()
#print(id(obj2))

print(add+add2)
print(add2 - sub)
print(div + div2)
