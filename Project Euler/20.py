i=1
f=1
while i<101:
    f=f*i
    i=i+1
print(f)
b=f
w=[]
while b!=0:
    a=b%10
    b=b//10
    w.append(a)
print(w)
i=0
s=0
while i<len(w):
    s=s+w[i]
    i=i+1
print("sum=",s)    
    
    
