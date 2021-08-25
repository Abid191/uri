n=int(input())
for i in range(n):
    a=int(input())
    c=int(a/2)
    d=0
    for j in range(1,c+1):
        if(a%j==0):
            d=d+j
    if(d==a):
        print(f"{a} eh perfeito")
    else:
        print(f"{a} nao eh perfeito")




