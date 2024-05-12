# FIND THE SECOND LARGEST NUMBER FROM A GIVEN LIST WITHOUT USING INBUILT FUNCTIONS

#l=[1,4,3,77,6,3,44,5,87,34,34,34,77,77,87,87]

'''s = set(l)
#print(s)
li = list(s)
print(li)'''
'''max1=l[0]
for i in range(1,len(l)):
    if(l[i]>max1):
        max1=l[i]
print(max1)'''

l=[1,4,3,77,6,3,44,5,87,34,34,34,77,77,87,87,90,90]
notdup = []

#CODE FOR REMOVING THE DUPLICATE ELEMENTS FROM THE LIST
for i in l:
    if i not in notdup:
        notdup.append(i) 
print(notdup)

srt = []
max1 = notdup[0]

#CODE FOR FINDING SECOND LARGEST ELEMENT
for i in range(0,len(notdup)):
    if notdup[i] > max1:
        max1 = notdup[i]
        #print(max1)
        srt.append(max1)
        #print(srt)
        
print('the Secnd laregest number inthe list is:',srt[-2])
    

        
