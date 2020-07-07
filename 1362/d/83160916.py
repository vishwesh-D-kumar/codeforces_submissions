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

def solve():
	n,m=I()
	graph=[[] for i in range(n)]
	for i in range(m):
		u,v=I()
		graph[u-1].append(v-1)
		graph[v-1].append(u-1)
	w=I()
	colors=[0]*n
	nodes=list(range(n))
	nodes.sort(key=lambda x:w[x])
	for node in nodes:
		currcolor=w[node]
		done=set()
		for neigh in graph[node]:
			if colors[neigh]!=0:
				done.add(colors[neigh])
		
		# print(done,currcolor,node)
		if done!=set(list(range(1,currcolor))):
			print(-1)
			return
		colors[node]=currcolor
	print(*[i+1 for i in nodes])





solve()
	



