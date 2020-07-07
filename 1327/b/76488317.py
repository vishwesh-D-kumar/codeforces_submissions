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
	n=int(input())
	arrs=[[]]*n
	doned=[False]*n
	donepr=[False]*n
	for i in range(n):
		arrs[i]=I()
		m=arrs[i][0]
		if m:
			for j in arrs[i][1:]:
				if not donepr[j-1]:
					donepr[j-1]=True
					doned[i]=True
					break


	d=-1
	p=-1
	for i in range(n):
		if not doned[i]:d=i+1
	for i in range(n):
		if not donepr[i]:p=i+1
	if d==-1 :print("OPTIMAL")
	else:
		print("IMPROVE")
		print(d,p)




