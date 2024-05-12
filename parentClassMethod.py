class Parent:

    def show(self):
        print('I am show from Parent class')


class Child(Parent):

    def show(self):
        print('I am  show from Child')

        #Calling the parent class method
        #Parent.show(self)
           #or both methods will work
        super().show()

c1 = Child()
c1.show()
#Parent.show(10)
