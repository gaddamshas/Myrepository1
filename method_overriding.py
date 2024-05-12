'''class A:
    def __init__(self):
        self.string = 'WE ARE TEAMED UP AS PSR'

    def display(self):
        print(self.string)

class B(A):
    def __init__(self):
        self.string = 'we are teamed up as psr'


    def display(self):
        print(self.string)



obj = B()
obj.display()
'''

#obj1 = A()
#obj1.display()


# Python program to demonstrate
# overriding in multiple inheritance


# Defining parent class 1
class Parent1():
		
	# Parent's show method
	def show(self):
		print("Inside Parent1")
		
# Defining Parent class 2
class Parent2():
		
	# Parent's show method
	def display(self):
		print("Inside Parent2")
		
		
# Defining child class
class Child(Parent1, Parent2):
		
	# Child's show method
	def show(self):
		print("Inside Child")
	
		
# Driver's code
obj = Child()

obj.show()
obj.display()

