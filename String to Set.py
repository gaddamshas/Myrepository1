#s = 'i am learning python'
s1 = {1,2,3}
s2 = {3,4,5,7}
#output = set(s)
#print(output)

#s1.update(s2)
#print(s1)
s = s2.difference(s1)
print(s) # gives output the elements which are not in s1 and there only in s2
