import numpy as np

a=map(int, input().split())
a=list(a)
cnt=0
for i in range(len(a)):
    while a[i]!=a[1]:
        if a[i]<a[1]:
            a[i]+=1
            cnt+=1
        elif a[i]==a[1]:
            i+=1
        elif a[i]>a[1]:
            a[i]-=1
            cnt+=1
print(cnt)
