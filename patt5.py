s = input(" Enter an string: ")
for i in range(0, len(s)):
    for k in range(0, len(s)-i):
        print(" ", end=" ")
        for j in range(0,i+1):
           print(s[j], end=" ")
           print()
