p,t,r=map(int,input().split())
CI=(p*(1+t/100)**r)
print('{:.2f}'.format(CI))