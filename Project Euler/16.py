x=2
y=1000
z=x**y
print(z)
w=[]
b=z
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
print("SUM=",s)
