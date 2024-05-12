import time
start = time.time()
i = 1
sum = 0
while i < 10000000:
    sum = sum + i
    i += 1
print(sum)
end = time.time()
print('total time taken by while loop',end-start)

