from itertools import count


t1 = (10,20,30,40,50,60,30,23,30)
t2 = (304,5,4,6,6,5,45,55,8)
t3=t1+t2

print(t3)

print(max(t3))

print(min(t3))

print(sum(t1))

print(t1.count(30))

print(sorted(t1,reverse=True))
print(len(t1),len(t2),len(t3))

#tuple packing

a = 10
b = 29
c = 23
d = 42
t = a,b,c,d
print(t)