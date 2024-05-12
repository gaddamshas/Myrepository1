class A:

    def __init__(self,a):
        self.a = a

    def info(self):
        print(self.a)

class B:

    def __init__(self,b):
        self.b = b

    def show(self):
        print(self.b)

class C(A,B):

    def __init__(self,c):
        self.c = c
        #calling super class constructor without using super(). __init__(self)
        A.__init__(self,c)
        B.__init__(self,c)
        #super().__init__(a,b)
        #super().__init__(a,b,c)

    def display(self):
        print(self.c)



c1 = C(10)
c1.info()
c1.show()
c1.display()
