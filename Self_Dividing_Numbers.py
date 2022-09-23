a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    if '0'in str(i):
        continue
    for j in str(i):
        if int(i)%int(j)==0:
            c+=1
    if len(str(i))==c:
        print(int(i),end=" ")