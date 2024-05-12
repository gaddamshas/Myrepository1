#LIST COMPREHENSION: It is a short way of creating the list based on some
#                    conditions


#Example 1

'''s = [n * n for n in range(1,21)]
print(s,'\n'*2)

#Example 2'''

print('Example 2')
s = [x**3 for x in range(1,11)]
print(s,'\n'*2)

#Prints only even number from above list s
m = [x for x in s if x % 2 == 0]
print(m)

n = ['1','2','3','4']
l = [num[0] for num in n]
print(l)
