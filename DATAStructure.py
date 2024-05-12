#LIST

#li = [1,2,3,4,5]
#print(li)

#nested list
'''li = [[1,2,3,4,5],[1,2,3,4,5]]
print(li)'''

#tuple in list
'''li1 = [1,'ram',2,3,2.5,(7,'mango','cat',10.5,10)]
print(li1)
print(type(li1))
idx = li1.index(2.5)
print(idx)
print(len(li1))'''

#set in list

'''li = [1,2,3,{1,3,5,6,3,'tomato','onion',5,'tomato',10.5},'tomato','onion',10.5]
print(type(li))
print(li)'''

#Dictionary in list

'''li = [1,2,3,{'veg':'tomato','name':'raj','age':21},'onion',10.5]
print(li)
print(type(li))'''

#TUPLE

#tup = (1,2,3,'raj',True,2+3j,3,2.5)
#
#list in tuple
'''tup = (1,2,3,'raj',[1,'ram',10.3,True],True,2+3j,3,2.5)
print(len(tup))
print(type(tup))
print(tup)'''

#tuple in tuple ==> nested tuple
'''tup = (1,(2,3,'raj'),[1,'ram',10.3,True],{1,3,4,4,4,4},True,2+3j,3,2.5,{'a':1,'b':'two'})
print(tup)
print(len(tup))'''

# Set

'''s = {1,2,'ram',10.5,3,1,2,4,5,6}
print(type(s))
print(s)'''

'''s = {1,2,(1,2,3),2,(4,5),6}
print(s)
print(type(s))'''

#Dictionary

'''dict = {'name':{'a':'raj'},'v':['ravi',1],'k':('age',32),'m':{1,2,3,4}}
print(dict)
print(type(dict))'''

a = [[10,20,30],[40,50,60],[70,80,90]]
print('Elements in row wise')
for i in a: 
    print(i)
print()
print('In matrix')
