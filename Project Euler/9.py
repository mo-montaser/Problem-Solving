import math
a=1
b=1
c=0
i=1
while a<1000:
    while b<1000:
        c=a*a+b*b
        c=math.sqrt(c)
        if a+b+c==1000 and a<b and b<c:
           
            s=a*c*b
            print("c=",c)
            print("b=",b)
            print("a=",a)
            print("product=",s)
            break
        b=b+1
    b=1
    a=a+1
print("the end")
