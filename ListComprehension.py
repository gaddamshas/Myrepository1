#LIST COMPREHENSION

'''output = []
for i in range(0,21):
    if i > 0 and i % 2 == 0:   #NORMAL METHOD
        output.append(i)
print(output)'''

#output = [i for i in range(0,21) if i> 0 and i % 2 == 0] #comprehension method
#print(id(output),'\n',output)


#output = [i ** 2 if i % 2 == 0 else i **3 for i in range(0,11)]
#print(output)

#output = [x*x for x in range(1,11)]
#print(output)

#words = ['nagas','meluha','triology']
#output = [i[4] for i in words]
#print(output)

#n1 = {'a':10,'b':20,'c':30,'d':40}    #try with other DS
#n2 = {'c':30,'d':40,'e':50,'f':60} 
#n3 = [i for i in n1 if i not in n2]   #check for not in
#print(n3)


n1 = [1,2,3,4,5,6,7,8]
#del n1[5]
#print(n1)
#del n1
#print(n1)
