def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a


n=int(input())
arr=I()
l=-1
d={0:-1}
prefix=[0]*(n+1)
prefix[0]=arr[0]
ans=0
for i in range(1,n):prefix[i]=arr[i]+prefix[i-1]
for i  in range(n):
	l=max(l,d.get(prefix[i],l-1)+1)
	d[prefix[i]]=i
	ans+=i-l
print(ans)