#li = [1,2,3,4,5,6,7,8,9]
squares = (lambda num = num : num ** 2 for num in range(0,10))
for square in squares:
    print(square(), end = ' ')

