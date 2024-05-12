import time
start = time.time()
#print(start)
sum = 0
for i in range(1, 10000000):
    sum = sum + i
print(sum)
end = time.time()
#print(end)
print('Total time taken by forloop', end - start)
  
