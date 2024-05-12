


'''class A:
    NAME = 'HHHHH'
    def __init__(self,name,age): 
        self.name = name
        self.age = age
        
    def show(self):
        print(A.name, A.age,A.NAME,ob2.NAME)
        
        
#ob = A('Ramesh', 24)

# #ob.show()
# class B(A):
    
#     def __init__(self,name,age):
#         self.name ='Flower'
        
#     def show(self):
#         print(ob2._name,ob2.age)
        


ob2 = A('Rachana',23)
ob2.show()

# ob2.name = 'Ramesh'
# ob2.show()
#print(A.mro())'''







'''class Grandfather:
 
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername



    def display(self):
        print(self.grandfathername)
 
# Intermediate class                                #G--->F(G)--->S(F)
 
 
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
 
        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

    def display(self):
        print(self.fathername)
 
# Derived class
 
 
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
 
        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def display(self):
        print(self.sonname)
 
    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)
 
 
#  Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()
s1.display()


        
    

class Parent:
    def func1(self):
        print("This function is in parent class.")
 
# Derived class1
 
 
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
 
# Derivied class2
 
 
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
 
 
# Driver's code
a = Child1()
a.func1()
a.func2()

b = Child2()
b.func1()
b.func3()    


a.func1()

a.func1()
b.func3()  '''






class Base:
    def __init__(self):
        self.a = "Geeks"
        self.c = "GeeksforGeeks"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)

obj2 = Derived()
#obj2.show()



