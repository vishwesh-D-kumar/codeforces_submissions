num=int(input())
mishka=0
chris=0
for i in range(num):
    game=list(map(int,input().split()))
    if game[0]>game[1]:
        mishka+=1
    if game[0]<game[1]:
        chris+=1
if mishka>chris:
    print("Mishka")
elif chris>mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")