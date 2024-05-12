#To create empty set
'''s  = set()
print(type(s))'''

'''s1 = {10,25,34,2,35,5}
s1.add(22)
print(s1)'''


from os import remove
from turtle import update


s = {10,20,30}
s1 = {40,50,60,20}
#s1 = l.copy()

#s.discard(20)# discard 20 #discard function will not work for list data structure
#s.discard(11) #will not throw error 
#s.remove(10) #removes 10 from the set
#s.remove(11) #throws error because 11 is not in the set
#print(l)
#print(s)
print(s1.intersection(s))
