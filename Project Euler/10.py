x=2
i=2
v=1
y=x
s=0
while x<2000000:
    z=0
    i=2
    while i<x:
        if x%i==0:
            z=1
            break
        i=i+1
    if z==0:
        y=x
        s=s+x
        print(v,"=",s)
        v=v+1
    x=x+1

print("End of the program")

#It takes " 00:04:32 " 
