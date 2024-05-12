n = [1,1,2,3,4,5,6,7,8,9]
i = 0
while i < len(n):
   
    print(n[i])
    i += 1

print('\nEnd of while loop\n')

 
for n1 in n: # iterates the list values
    print(n1)

print('\nEnd of for loop\n')

for n1 in n:
    if n1 > 0 and n1 % 2 == 0:
        print(n1)

print('\nEnd of Even number\n')

l = [10,38,3,2,5,6,112,45,67]
for i in range(len(l)): #iterates the index numbers
    print(i)
