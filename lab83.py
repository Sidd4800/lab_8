
# Online Python - IDE, Editor, Compiler, Interpreter
l1 = list(map(int,input().split()))
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
print(l1)            
 
