while(True):
    a=int(input())
    if(a==0):
        break
    r= ""
    for i in range(1,a+1):
        r +=str(i)+" "
    print(r[:-1])

