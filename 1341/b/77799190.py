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
	peaks=[0]*(n+1)
	p=[0]*n
	c=0
	for i in range(1,n-1):
		if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
			peaks[i]=peaks[i-1]+1
			p[i]=1
		else:
			peaks[i]=peaks[i-1]
			p[i]=0
	peaks[n-1]=peaks[n-2]
	# print(peaks)
	# print(p)
	m=0
	idx=0
	for i in range(n-k+1):
		m_curr=peaks[k+i-1]-peaks[i-1]
		m_curr-=(p[k+i-1]+p[i])
		# print(m_curr)
		if m_curr>m:
			m=m_curr
			idx=i
	print(m+1,idx+1)



	



