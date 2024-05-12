#OBJECT ORIENTED PROGRAM

class Triangle:

#Constructor function, it is a special method which will be invoked automatically
#when object is created.
    TRIANGLE = 'VOLUME OF TRIANGLE'
    def __init__(self,base,height): #self-->It is a current object

        #Instance Variables
        self.__base = base     #By using '__' we are making our data private
        self.__height = height # so it cannot be modified/accessed outside the class


    def getVolume(self): 
        print(Triangle.TRIANGLE)
        volume = (self.__base * self.__height) / 2
        return volume


#print(Triangle.TRIANGLE)
obj1 = Triangle(12,15)
obj1.base = 5               #In Oops also we can modify data, if we donot make 
volume1 = obj1.getVolume() #variable as private
#print(obj1.TRIANGLE)
print(volume1)

# obj2 = Triangle(15,20)
# volume2 = obj2.getVolume()
# #print(obj2.TRIANGLE)
# #print(Triangle.TRIANGLE)
# print(volume2)

#obj1.getVolume()
#print(obj1.TRIANGLE)
# print(Triangle.TRIANGLE)
# print(volume1)
#print(obj2.TRIANGLE)
# print(Triangle.TRIANGLE)
# print(volume2)







                
    
