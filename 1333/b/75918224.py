def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a




for __ in range(int(input())):
	n=int(input())
	a,b=I(),I()
	f=0
	done={1:0,-1:0,0:0}
	for i in range(n):
		if (b[i]>a[i] and not done[1]) or (b[i]<a[i] and not done[-1]):
			f=1
			break
		done[a[i]]=1
	print(["YES","NO"][f])

