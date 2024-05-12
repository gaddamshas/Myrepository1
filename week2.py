words = '''JIT
(Just In Time compiler)
enables
high
performance in Java. JIT converts a the bytecode a into machine language a and then JVM starts the execution'''
word = words.split()
distinct = []
cnt = []


for i in word:
    c = words.count(i)
    
    if i not in distinct:

        distinct.append(i)
        cnt.append(c)
         
print(len(distinct))
print(cnt)
