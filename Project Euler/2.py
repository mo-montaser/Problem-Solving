a=[1]
s=0
end=0
#################
while a[-1]<4000000:

    for i in a:
        s=s+a[-1]
        a.append=(s)

    for i in a:
        if i%2==0:
            end=end+i
