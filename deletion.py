a=[1,2,10,3,4,5]
def delete(ind,a):
    c=[0 for i in range(len(a)-1)]
    for i in range(0,ind):
        c[i]=a[i]
    for i in range(ind,len(a)-1):
        c[i]=a[i+1]
    return c
a=delete(2,a)
print(a)
a=delete(2,a)
print(a)


def delete(a,ind):
    ar=[0 for i in range(len(a)-1)]
    for i in range(ind):
        ar[i]=a[i]
    for i in range(ind+1, len(a)):
        ar[i-1]=a[i]
    return ar
a=delete(a,2)
print(a)