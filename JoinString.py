li = ['Raj','Ravi','Shashi','Shree','Shra','Sachi'] #o/p=> Raj-Ravi....-Sachi

#normal logic
newstr = '' # nothing
#for i in li:
#for i in range(0, len(li)):# 0
    #if i == len(li) - 1: #0==5, 1==5, 2==5...5==5
    #    newstr = newstr + li[i] #Raju-Rav-....-Sachi

   # else:
       # newstr = newstr + li[i] + ' - '  #Raju-Ravi-....
#print(newstr)

#python method
newstr = ' - '.join(li)
print(newstr)
