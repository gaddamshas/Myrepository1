t = (x * 2 for x in range(1,10))
print(t) #here we are not getting tuple object and we are getting generator object
print(type(t))
for x in t:
    print(x,end=' ')