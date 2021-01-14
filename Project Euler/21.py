x=1
y=1
s=0
z=0
t=0
while x<10000:
    #
    i=1
    t=0
    while i<x:
        
        if x%i==0:
            t=t+i
        i=i+1
        ##@@@@@@@@@@@@@@@
    j=1
    z=0
    while y<10000:
        ##
        while j<y:
            ####
            if y%j==0:
                z=z+j
            j=j+1
        print(y)
        y=y+1
    if x==z:
        s=s+z+t
        ##@@@@@@@@@@@@@@@@@@

    print(x,"\n****************************")
    x=x+1
    
print("s=",s)    
print("The end")
