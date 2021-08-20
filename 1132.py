a=int(input())
b=int(input())
temp=a
sum=0
if(a>b):
    a=b
    b=temp
while(a<=b):
    if(a%13 !=0):
      sum=sum+a
    a=a+1
print(sum)

