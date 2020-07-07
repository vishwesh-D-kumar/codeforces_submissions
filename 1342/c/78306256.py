import sys
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	a,b,q=I()
	pref=[0]*(a*b)
	pref[0]=1

	for i in range(1,a*b):
		if i%a%b==i%b%a:
			pref[i]=pref[i-1]+1
		else:
			pref[i]=pref[i-1]


	for lol in range(q):
		l,r=I()
		l-=1
		tillL=pref[-1]*(l//(a*b))+pref[l%(a*b)]
		tillR=pref[-1]*(r//(a*b))+pref[r%(a*b)]
		print(r-l-(tillR-tillL),end=" ")
	print()


	



