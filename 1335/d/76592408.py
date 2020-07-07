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
def f(i,j):
	matr[i][j]=matr[i][j]+1 if matr[i][j]<=8 else 1
for __ in range(int(input())):
	matr=[[]]*9
	for i in range(9):
		matr[i]=[int(j) for j in input()]
		# print(matr[i])
	# print(matr)
	# print(matr)
	# for j in range(3):
	# 	for i in range(3*j,9):
	# 		matr[i][j]=matr[i][j]+1 if matr[i][j]<=8 else 1
	# 		print(i,j)
	# 		j+=3

	f(0,0)
	f(1,3)
	f(2,6)
	f(3,1)
	f(4,4)
	f(5,7)
	f(6,2)
	f(7,5)
	f(8,8)


	# print(matr)
	# matr[0][0]
	for i in range(9):
		s=""
		for j in range(9):
			s+=str(matr[i][j])
		print(s)




