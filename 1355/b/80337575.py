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
	arr=I()
	arr.sort()
	grps=[[arr[0]]]
	maxgroups=[arr[0]]
	curr=0
	for i in range(1,n):
		if maxgroups[curr]>len(grps[curr]):
			maxgroups[curr]=arr[i]
			grps[curr].append(arr[i])
		else:
			grps.append([[arr[i]]])
			maxgroups.append(arr[i])
			curr+=1
	c=0
	for i in range(len(grps)):
		if len(grps[i])>=maxgroups[i]:c+=1
	# print(grps)
	# print(maxgroups)
	print(c)



	



