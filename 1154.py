a=0
sum=0
b=0
while(True):
    a=int(input())
    if(a>=0):
        sum=sum+a
        b=b+1
    else:
        break
print("%.2f"%(sum/float(b)))




