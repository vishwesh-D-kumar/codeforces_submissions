
y=input()
x=input()
z=x+y
k=input()
flag=0
for i in z:
    if z.count(i)!=k.count(i) or len(k)!=len(z) :
        flag=1

if flag==0:
    print("YES")
else:
    print("NO")
    