a=int(input())
n=list(map(int, input().strip().split()))
m=sum(n)
if m%2==0:
    print(1)
else:
    print(0)