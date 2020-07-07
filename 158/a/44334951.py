y=list(map(int,input().split()))
n=y[0]
k= y[1]
c=0
scores=list(map(int,input().split()))
for i in scores:
    if i>= scores[k-1]  and i>0:
        c+=1
        
print(c)