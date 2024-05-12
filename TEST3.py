list1 = []
winner= []
n = int(input('Enter the numberb of participants:'))
for i in range(0, n):
    print(f'Enter score {i}th score:')
    s = int(input())
    list1.append(s)
#print(list1)

for i in range(0, len(list1)):
    #print(i, end=' ')
    min_val = min(list1[i:])
    idx = list1.index(min_val)
    list1[i],list1[idx] = list1[idx],list1[i]
#print(list1)

for i in range(0, len(list1)):

    if i not in list1:
        winner.append(i)

print(list1[-1])
