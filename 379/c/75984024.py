n=int(input())
arr=list(map(int,input().split()))
l=sorted(list(range(n)),key=lambda x:arr[x])
# print(arr)
ans=[-1]*n
m=arr[l[0]]
for i in l:
	c=max(m,arr[i])
	ans[i]=c
	m=c+1
print(*ans)



