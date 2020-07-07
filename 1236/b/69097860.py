def I(): return(list(map(int,input().split())))
n,m=I()
x=pow(2,m,1000000007)
print(pow(x-1,n,1000000007))
