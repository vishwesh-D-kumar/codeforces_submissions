num=input()
ans=0
for i in range(int(num)):
    list=map(int,input().split())
    sum=0
    for i in list :
        sum+=i
    if sum>=2:
        ans+=1 
print(ans)
