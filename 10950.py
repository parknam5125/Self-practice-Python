t=int(input())
r=[]
for i in range(t):
    a,b=map(int,input().split())
    r.append(a+b)
for i in range(t):
    print(r[i])