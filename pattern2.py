s = input("Enter any string: ")
for i in range(0, len(s)):
    for j in range(0, len(s)-i):
        print(s[j], end = " ")
    print()
