a,b=map(int,input().split())
c=int(input())
s = a*60+b+c
if s>=1440:
    s=s%1440
    h=s//60
    m=s-60*h
    print('%d %d'%(h,m))
else:
    h=s//60
    m=s-60*h
    print('%d %d'%(h,m))