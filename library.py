import sys
print(sys.version)

from datetime import datetime
num = range(1, 60)
num = datetime.today().minute
if(num % 2 == 0):
    print("Even minute")
else:
    print("Odd minute")
