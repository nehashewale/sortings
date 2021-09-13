n=12
wt=n/2
a=[]
for i in range(n):
    a.append(i)
for i in range(n):
    a[i]=(0,2^n)
    
    
    
e=[]
wte=0
for i in range(n):
    e.append(i)
while(wte!=n/2):
    wte=0
    for i in range(n):
        for j in (0,2):
            e.append(j)
            wte=wte+e[j]
print(a)
print(e)
t=0
for i in range(n):
    t=t+a[i]*e[i]
t=t%2^n
    
print(t)