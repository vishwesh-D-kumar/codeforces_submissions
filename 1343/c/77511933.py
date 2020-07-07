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

# m_max=10**9+1
m_min=-10**9-1
for __ in range(int(input())):
	n=int(input())
	arr=I()
	i=0
	s=0
	while(i<n):
		
		if arr[i]<0:
			s_min=m_min
			while(i<n and arr[i]<0):
				s_min=max(arr[i],s_min)
				i+=1
			s+=s_min
		else:
			s_max=-1
			while(i<n and arr[i]>0):
				s_max=max(arr[i],s_max)
				i+=1
			s+=s_max
		
	print(s)






