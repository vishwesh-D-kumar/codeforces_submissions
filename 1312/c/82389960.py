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
	n,k=I()
	arr=I()
	c=1
	used=[0]*100
	ans="YES"

	for i in range(n):
		a=arr[i]
		basek=[]
		i=0
		while(a):
			# basek.append(a%k)
			
			if a%k!=0:

				if (used[i]==1) or a%k>1:
					ans="NO"
				used[i]=1
			i+=1
			a//=k
		# basek=basek[::-1]
		# print(basek)
	print(ans)



	



