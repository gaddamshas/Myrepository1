#PROCEDURE ORIENTED PROGRAM

#Function for VOLUME OF TRIANGLE
def volumeOfTriangle(base,height):

    volume = (base * height) / 2 

    return volume

base = 12
height = 15
height = 20    #Here data can be easily changed so, there is no data security
               #in POP

base2 = 10
height2 = 20
base2 = 20     #Here data can be easily changed so, there is no data security
               #in POP

tri_volume = volumeOfTriangle(base,height)
print('Volume of triangle is',tri_volume)

tri_volume = volumeOfTriangle(base2,height)
print('Volume of triangle is',tri_volume)
