d = {1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:90}
print(type(d))
print(d)

#Creating a dictionary with values with runtime
d = {}
n = int(input('Enter how may key value pairs you want to insert into dictionary: '))
for i in range(1, n+1):
    k = eval(input("Enter key: "))
    v = eval(input("Value: "))
    d[k] = v
print(d)

pb = {}
pb[1] = 958685
pb[2] = 768594
pb[3] = 6785940
print(pb)
