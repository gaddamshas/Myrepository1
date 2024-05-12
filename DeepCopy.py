list1 = [1,2,3,4,5]
list2 = []

list2.extend(list1)


print(id(list1))
print(id(list2))

print(list1)
print(list2)

list1.append(120)

print(list1)
print(list2)
