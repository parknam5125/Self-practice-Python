a,b=map(int,input().split())
if (a==0)&(b<45):
    c=a*60+b-45+1440
    h=c//60
    m=c-h*60
    print('%d %d'%(h,m))
else:
    c=a*60+b-45
    h=c//60
    m=c-h*60
    print('%d %d'%(h,m))
