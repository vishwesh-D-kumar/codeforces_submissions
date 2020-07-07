n,m,a=map(int,input().split())
d1=m//a 
d2=n//a
if m%a!=0:
    d1=d1+1
if n%a!=0:
    d2=d2+1
print(d1*d2)