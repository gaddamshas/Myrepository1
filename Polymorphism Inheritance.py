#POLYMORPHISM : Same piece of code is cahnging its behaviour according to the
              # situation.

#example


class Dog:

    def sounds(self):

        print('Bow Bow')

class Cat:

    def sounds(self):

        print('Meow Meow')

class Pig:
    def sounds(self):

        print('Dhoark Dhoark')

        
def call(object1):
    object1.sounds()


c = Cat()
call(c)

d = Dog()
call(d)

p = Pig()
call(p)

print('')
#example2
class Circle:

    def type(self):
        print('I am circle')

class Triangle:

    def type(self):
        print('I am Triangle')

class Rectangle:

    def type(self):
        print('I am Rectangle')

class Pentagon:

    def type(self):
        print('I am Pentagon')

def call(obj):
    obj.type()

c = Circle()
call(c)

t = Triangle()
call(t)

r = Rectangle()
call(r)

p = Pentagon()
call(p)
