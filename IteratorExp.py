li = [1,2,3]

iterator = iter(li)

print('First iteration')
print(next(iterator))
print('End of first iteration')




print('Second iteration')
print(next(iterator))
print('End of second iteration')




print('Third iteration')
print(next(iterator))
print('End of third iteration')#till here it execute properly




print('Fourth iteration')   #beyond the range Error: stop iterator
print(next(iterator))
print('End of Fourth iteration')





