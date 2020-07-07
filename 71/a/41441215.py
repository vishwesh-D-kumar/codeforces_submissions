n=input()
i=0
for i in range(int(n)):
    word=input()
    if len(word)>10:
        length=len(word)-2
        ans=word[0]+str(length)+ word[-1]
    else:
        ans=word

    print (ans)
    i+=1