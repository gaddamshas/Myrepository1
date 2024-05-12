class A:

    SCHOOL_NAME = 'CLASS A'
    print(SCHOOL_NAME)
    

    def display(self):
        print(A.SCHOOL_NAME)
        print('I am display from class A')

class B(A):
    

    def display(self):

        print('I am display from class B')

b1 = B()
b1.display()
print(A.SCHOOL_NAME)
#print(B.SCHOOL_NAME)
