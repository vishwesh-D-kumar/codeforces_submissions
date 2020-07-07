import sys
# input = sys.stdin.buffer.readline
from collections import deque
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a
def check(i,j):
	if matr[i][j]=="B":
		for x,y in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
			if x>=0 and y>=0 and x<n and y<m:
				if (x,y)==(n-1,m-1):
					return False
				if matr[x][y]=="G":
					return False
	return True
def bfs(i,j,good):
		q=deque()
		q.append((i,j))
		visited=set()
		while(q):
			u,v=q.popleft()
			if (u,v) in visited:
				continue
			visited.add((u,v))
			for x,y in getneighs(u,v):
				if "B" in [matr[t][l] for t,l in getneighs(x,y)]:
					continue
				q.append((x,y))
		for g in good:
			if g not in visited:
				return False 
		return True





def getneighs(i,j):
	neighs=[]
	for x,y in (i+1,j),(i-1,j),(i,j-1),(i,j+1):
		if x>=0 and y>=0 and x<n and y<m and matr[x][y]!="#":
			neighs.append((x,y))
	return neighs
for __ in range(int(input())):
	n,m=I()
	good=False
	goods=set()
	matr=[[] for i in range(n)]
	for i in range(n):
		matr[i]=[j for j in input()]
		if not good:
			if "G" in matr[i]:
				good=True
	if not good:
		print("Yes")
		continue
	f=True
	for i in range(n):
		for j in range(m):
			if not check(i,j):
				f=False
			if matr[i][j]=="G":
				goods.add((i,j))
		if not f:
			break

	if f:
		if not bfs(n-1,m-1,goods):
			f = False

	if f:
		print("Yes")
	else:
		print("No")






