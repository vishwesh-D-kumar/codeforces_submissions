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
	n,m=I()
	donerows=set()
	donecols=set()
	matr=[[] for i in range(n)]
	for i in range(n):
		matr[i]=I()
		for j in range(m):
			if matr[i][j]==1:
				donerows.add(i)
				donecols.add(j)
	todo=min(n-len(donerows),m-len(donecols))
	if todo%2==0:
		print("Vivek")
	else:
		print("Ashish")	



