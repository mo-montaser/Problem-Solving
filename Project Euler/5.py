i=1
x=2
z=0
while x>0:
    i=1
    while i<21 and x%i==0:
        
        if i==20:
            z=1
        i=i+1

    if z==1:
        print("the number =",x)
        break
    print("x=",x)
    x=x+1

print("The End")
        
        
