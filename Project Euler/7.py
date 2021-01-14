x=2
i=2
v=1
y=x
while v<10002:
    z=0
    i=2
    while i<x:
        if x%i==0:
            z=1
            break
        i=i+1
    if z==0:
        y=x
        print(v,"=",y)
        v=v+1
    x=x+1

print("End of the program")

#It takes " 00:04:32 " 

        
            
        
        
