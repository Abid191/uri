while(True):
    sum=0
    a=0
    x=int(input())
    if(x==0):
        break
    if(x%2!=0):
        x=x+1
    for i in range(5):
        sum=sum+x
        x=x+2
    print(sum)


