#SET : Data structure which stores the heterogenous data which can be modified
#      and it will not support duplicate values i.e mutable which donot follow
#      order, so there is no index value hence we cannot use slicing operation.

#syntax
# setname = {value,...}
#eg
#s = {True,2,'Ram',1,10.5,2+3j,'raj',2,3,1,1,}
#print(s)
#s.add('Siva') #adds Siva to set

s1 = {10,1,'Raj'}

s2 = {10,True,3,'Ram',10.5}

#s = s1.union(s2)
#s = s1.intersection(s2)
#s = s1.symmetric_difference(s2) # gives the val which present in one set and not
                                #in other 
s2.update(s1)
print(s2)

 
