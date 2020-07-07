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
    matr = [[] for i in range(n)]
    for i in range(n):
        matr[i]=I()
    # ans=0
    # for i in range(n):
    #     x=i
    #     c1=0
    #     c2=0
    #     for j in range(min(i,m)):
    #         x1=x-j
    #         y1=j

    #         x2=(n-1-x1)
    #         y2=(m-1-y1)
    #         print(x1,y1)
    #         print(x2,y2)
    #         if matr[x1][y1]!=1:
    #             c1+=1
    #         else:
    #             c2+=1
    #         if matr[x2][y2]!=1:
    #             c1+=1
    #         else:
    #             c2+=1
    #     ans+=min(c1,c2)
    # print(ans) 
    ans=0
    # There will be n+m-1 lines in the output 
    for line in range(1, (n + m)) : 
        # Get column index of the first element 
        # in this line of output. The index is 0 
        # for first n lines and line - n for 
        # remaining lines  
        start_col = max(0, line - n) 
  
        # Get count of elements in this line. 
        # The count of elements is equal to 
        # minimum of line number, m-start_col and n  
        count = min(line, (m - start_col), n) 
        c1=c2=0
        # Print elements of this line  
        for j in range(0, count) : 
            x1=min(n, line) - j - 1
            y1=start_col + j
            x2=(n-1-x1)
            y2=(m-1-y1)
            # print(x1,y1,x2,y2)
            if x1+y1==x2+y2:
                # print("continue")
                continue
            
            # print(x2,y2)
            if matr[x1][y1]!=1:
                c1+=1
            else:
                c2+=1
            if matr[x2][y2]!=1:
                c1+=1
            else:
                c2+=1
        # print("###")
        ans+=min(c1,c2)
    print(ans//2)



            







