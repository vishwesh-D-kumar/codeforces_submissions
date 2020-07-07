import sys
# input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n,m,x,y=I()
	c=0
	doubles=0
	singles=0
	for i in range(n):
		arr=input()
		i=0
		singles+=arr.count(".")*x
		while(i<m-1):
			if arr[i]=="." and arr[i+1]==".":
				doubles+=y
				i+=2
				continue
			if arr[i]==".":
				doubles+=x
			i+=1
		if i==m-1 and arr[i]==".":
			doubles+=x
	# print(singles,doubles)
	if doubles==0:
		print(singles)
		continue
	print(min(singles,doubles))


	



