li = [1,2,3,4,5,6]

'''def square(num):

    return num ** 2'''

'''for i in li:
    res = square(i)
    print(res)'''

'''res = map(lambda num:num ** 2, li)

print(list(res))'''


res = list(map(lambda num: num ** 3, li))
print(res)
