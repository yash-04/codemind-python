
a=int(input())
b=int(input())
p_a=p_b=0
for i in range(1,a):
    if a%i==0:
        p_a+=i
for i in range(1,b):
    if b%i==0:
        p_b+=i
if(p_a==b and p_b==a):
    print('Amicable')
else:
    print("Not Amicable")