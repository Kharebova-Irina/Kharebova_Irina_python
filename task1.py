import numpy as np
numbers=int(input('Введи число: '))
step=1
list_1=[]
for i in range(1, numbers+1):
    list_1.append(i)
k=len(list_1)
a=np.zeros(3*len(list_1))

start=1
end=start+step
i=1
a[0]=list_1[0]
while i!=len(a)-1:
    for i in range(start, end, step):
        a[i]=list_1[i%k]
    start=end
    end=start+step
list_2=[]
m=len(a)
for i in range(0, m, 3):
    list_2.append(int(a[i]))
list_2
