#Abstraction : Hinding some implementation from outside the world

from abc import ABC, abstractmethod #abc->module, ABC->class

class Animal(ABC):
   print()
  
    #def sounds(self):
@abstractmethod        #pass
class Dog(Animal):

    def sounds(self):
        print('Bow Bow')


class Cat(Animal):

    def sounds(self):
        print('Meow Meow')

#ob = Animal()       #ob = Animal()
#ob.sounds()         #TypeError: Can't instantiate abstract class Animal
                    #with abstract method sounds'''

obj1 = Cat()
obj1.sounds()

obj2 = Dog()
obj2.sounds()


