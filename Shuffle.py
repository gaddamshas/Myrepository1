   import random

li = [1,2,3,4,5,6,7,8,9]
print(li)
'''li = []
num = int(input('Enter the number of elements to be inserted into the list: '))

for i in range(0,num):
    elements = int(input())
    li.append(elements)
print('Entered order = ',li)'''

output = []
indexes = []

for i in range(0,100000):    
    idx = random.randint(0,len(li)-1) #1 to 9
    if idx not in indexes:
        output.append(li[idx])
        indexes.append(idx)

    if len(li) == len(output):
        break
print('Shuffled order = ',output)
