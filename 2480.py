a,b,c=map(int,input().split())
m=0
if(a==b)&(b==c):
    m=10000+a*1000
elif (a==b):
    m=1000+100*a
elif (b==c):
    m=1000+100*b
elif (a==c):
    m=1000+100*a
else:
    m=max(a,b,c)*100
print(m)