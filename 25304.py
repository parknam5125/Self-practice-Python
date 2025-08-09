sum=int(input())
cnt=int(input())
p=[]
c=[]
for i in range(cnt):
    a, b = map(int, input().split())
    p.append(a)
    c.append(b)
m=0
for i in range(cnt):
    m+=p[i]*c[i]
if m==sum:
    print('Yes')
else:
    print('No')